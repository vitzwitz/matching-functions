import scipy.misc as sm
import motifFunctions as cmd
import os
import pandas as pd
global d
import copy
import math as m


def MaptoString(motif, distances, comparisons):
    newMaps = []

    for pair in distances:

        newMaps.append(str(pair[0]) + "_" + str(pair[1]))
        motif += str(pair[0]) + "_" + str(pair[1]) + \
                         " = { \n" + "\t'distances'" + ":\n\t\t" + str(distances[pair]) + ",\n"
        motif += "\t'comparisons'" + ":\n\t\t" + str(comparisons[pair]) + "}\n"
    return motif, newMaps


def parseMotifFiles(newFiles):

    # loop through old motif files
    for file in newFiles:

        # Initialize variables
        filename = ""
        motif = ""
        flag_info = False
        pairs = []
        mtrx = {}
        comparisons = {}
        index = 1

        # loop through lines in motif
        for line in open(file):
            line = str(line)
            # Skip if line consists a delete call
            if line[4:10] == "delete":
                pass

            # Adding Motif Info and creating file name
            elif line.strip("\n") == "'''" and flag_info == True:
                motif += line
                motif += "import motifFunctions as cmd\n"
                flag_info = False

            elif flag_info == True:
                motif += line
                if line[0:4] == "FUNC":
                    filename = line[5:len(line)-1]
                    if filename[0] == "J":
                        break
                elif line[0:4] == "RESI":
                    res = line[5:].strip("\n").split(",")
                    num = m.factorial(len(res))/m.factorial(len(res) - 2)
                    resPairs = []

                    resCombos = []
                    for i in range(len(res)):
                        for j in range(len(res)):
                            if i != j:
                                combo = (res[i].upper(), res[j].upper(), 0)
                                resCombos.append(combo)

                    if len(resCombos) != num:
                        print "Test: Residue combos list produced incorrectly"
                        print "\tCorrect Number:"
                        print "\tActual Number: ", len(resCombos)



            elif line == "'''\n" and flag_info == False:
                motif += line
                flag_info = True


            # Lines that are possible comparisons
            if line[4:10] == "select" and line.split(",")[1][2] == "n":

                pymol = line.split(",")
                name = ""
                for c in pymol[0].strip("cmd.select("):
                    if ord(c) >= 97:
                        name += c

                sele = pymol[1].split("%")
                if len(sele) > 1:

                    if len(sele) != 3:
                        raise Warning
                    try:
                        selection = ((sele[0] + "%" + sele[1]).strip(" '").strip("'")) %float(sele[-1].strip("'(d*").strip("))\n'"))
                    except ValueError:
                        print "Test 15 - Selection Algebra:\n"
                        print "Filename:", filename
                        print sele
                    data = cmd.select(name=name.upper(), selection=selection, comparisons=comparisons, matrices=mtrx, resPairs = resPairs, motifname = filename)

                    # Skips extra comparisons
                    if data == None:
                        pass
                    else:
                        comparisons, mtrx, resPairs = data

                        # Old method
                        # if flag == True:
                        #     if resPair not in res:
                        #         if j == len(pairs):
                        #             raise Warning
                        #         pairs[j] = resPair
                        #         j+=1
                        #     break
            index += 1

        """
         Test 1 contains:
            1. Boolean if test passes or fails
            2. String of results if test fails
         Test 2 contains:
            1. Boolean if test passes or fails
            2. String of results if test fails, empty string if test passes
        """

        t1Comp, t2Comp = cmd.testConstruction(map=comparisons, numPairs=num, pairs=copy.deepcopy(resCombos))
        t1Mtrx, t2Mtrx = cmd.testConstruction(map=mtrx, numPairs=num, pairs=copy.deepcopy(resCombos))


        results = ""
        # 1-> If tests fail
        # 2-> If missing data
        # 3-> If ill-produced data
        if t1Comp[0] or t1Mtrx[0] or t2Mtrx[0] or t2Comp[0] or \
                        len(t2Comp[1]) > 0 or len(t2Comp[1]) > 0:
            results += "Motif " + filename + " has been improperly created\n"

            if t1Comp[0] or t1Mtrx[0]:

                results += "Test 1 -> "
                results += "\nIssue: Ill-produced matrices inside"

                if t1Comp[0]:
                    results += "\t\t ***** comparisons map *****\n"
                    results += "   " + t1Comp[1] + "\n"
                    results += "================================================\n"

                if t1Mtrx[0]:
                    results += "\t\t ***** distance map *****\n"
                    results += "   " + t1Mtrx[1] + "\n"
                    results += "================================================\n"

            if t2Comp[0] or t2Mtrx[0]:

                results += "Test 2 -> "
                results += "\nIssue: Incorrect number of residue pairs \n"

                if t2Comp[0]:
                    results += "\t\t ***** comparisons map *****\n"
                    results += "   " + t2Comp[1] + "\n"
                    results += "================================================\n"

                if t2Mtrx[0]:
                    results += "\t\t ***** distance map *****\n"
                    results += "   " + t2Mtrx[1] + "\n"
                    results += "================================================\n"
            print results
            testIdx = 0
            while True:
                more = raw_input("Do you want more information? ")
                if more == "Y" or more == "y":
                    if testIdx == 0:
                        print cmd.moreTests(resCombos, comparisons, res, num)
                    elif testIdx == 1:
                        print cmd.moreTests(resCombos, mtrx, res, num)
                    elif testIdx == 2:
                        print "Compare rows in matrix for each pair"
                        for ky in comparisons:
                            matrix = comparisons[ky]
                            skele1 = []
                            for row in matrix:
                                skele2 = []
                                skele1.append(row[0][0])

                                for ele in row:
                                    skele2.append(ele[2])

                                print "\tRES 2 <", row[0][3], ">",  skele2
                            print "\tRES 1 <", matrix[0][0][1], ">", skele1, "\n"
                    elif testIdx == 3:
                        print "FInd source of issue by analyzing distance matrix"
                        for key in mtrx:
                            ill = False
                            rslts = "Pair <" + str(key) + ">\ny" \
                                                          ""
                            matrix = mtrx[key]

                            start = len(matrix[0])
                            for row in matrix:
                                rslts += str(row) + "\n"
                                if len(row) != start:
                                    ill = True


                            print rslts + "\n"
                    elif testIdx == 4:
                        print "**** comparisons map *****"
                        for pr in comparisons:
                            matrix = comparisons[pr]

                            print "<", pr, ">"
                            for row in matrix:
                                print "ROW SIZE ->", len(row)
                            print "\n"

                    elif testIdx == 5:
                        print "**** distance map *****"
                        for pr in mtrx:
                            matrix = mtrx[pr]

                            print "<", pr, ">"
                            for row in matrix:
                                print "ROW SIZE ->", len(row)
                            print "\n"
                    else:
                        print "No more options! Choose N/n"
                    testIdx += 1
                elif more == "N" or more == "n":
                    cont = raw_input("Do you want the program to continue? ")
                    if cont == "Y" or cont == "y":
                        break
                    else:
                        quit()
                else:
                    print "Please answer with Y or y for yes & N or n for no"



        # Convert Comparison and Distance maps into a map for each residue pair:
        #       - key = "distance"   : value = distance matrix
        #       - key = "comparison" : value = comparison matrix
        motif, newMaps = MaptoString(motif=motif, distances=mtrx, comparisons=comparisons)


        idx = 1
        flag = False
        motif += "\n\nflag = False\n"
        motif += "while True:\n"
        for pair in newMaps:
            motif += "\tmatch" + str(idx) + " = " + "cmd.detect(" + str(pair) + ", d, '" + filename + "')\n"

            motif += "\tif match" + str(idx) + " == " + "[]:\n"
            motif += "\t\t flag = True\n"
            motif += "\t\t break\n"
            motif += ""

            if idx == len(newMaps):
                motif += "\tbreak\n"

            idx +=1

        flag = False
        idx = 1
        for pair in newMaps:
            if len(newMaps) > 1:
                if flag == False:
                    motif += "\nif flag == False:\n"
                    motif += "\tmatches" + " = " + "{\n\t\t" + pair + ": match" + str(idx) + ","
                    flag = True
                else:
                    if idx < len(newMaps):
                        motif += "\n\t\t" + pair + ": match" + str(idx) + ","
                    else:
                        motif += "\n\t\t" + pair + ": match" + str(idx) + "}"
            else:

                motif += "\nmatches = {\n\t\t\t" + pair + ": match" + str(idx) + "}"
            idx += 1


        if filename == "" or motif == "":
            print "Didn't create anything"
            raise Warning

        # Source: https://stackoverflow.com/questions/11700593/creating-files-and-directories-via-python

        if filename[0] != "J":
            path = 'Motifs_old'
            filename += '.py'
            if not os.path.exists(path):
                os.makedirs(path)

            with open(os.path.join(path, filename), 'wb') as temp_file:
                temp_file.write(motif)

def parseNewMotifFiles(newFiles):
    # loop through old motif files
    for file in newFiles:
        flag = False
        motif = ""
        filename = ""
        count = 0
        for line in open(file):
            line = str(line)

            if line[:4] == "FUNC":
                filename = line[5:].strip("\n") + ".py"
            # if line[:4] == "RESI":
            #     reS = sm.comb(len(line[5:].split(",")),2)
            #     res = line[5:].split(",")

            if line == "if flag == False:\n":
                motif += line
                flag = True

            # For 1st update
            # elif line == "\tmatches = {\n":
            #     flag = True
            #     motif += line

            elif flag == True:
                if line == "\tmatches = {\n":
                    motif += line
                else:
                    temp = line.strip("").split(":")
                    temp2 = temp[0].strip("\t").split("_")
                    motif += "\t\t'" + temp2[0] + "_" + temp2[1] + "' : " + temp[1]
                    count += 1

            else:
                motif += line


        if filename == "":
            print "Error: Did not find motif name"
            quit()

        if filename[0] != "J":
            # Writes and adds motif file to new directory
            path = 'Motifs_2.0'
            if not os.path.exists(path):
                os.makedirs(path)
            with open(os.path.join(path, filename), 'wb') as temp_file:
                temp_file.write(motif)

def checkLines(newFiles):
    a = 0
    m = 0
    p = 0
    pab = 0
    pfa = 0
    r = 0
    # =====
    ca = 0
    cm = 0
    cp = 0
    cpab = 0
    cpfa = 0
    cr = 0

    total = []
    filename = ""

    for file in newFiles:
        count = 0
        flag = False
        for line in open(file):
            line = str(line)

            if line[:4] == "FUNC":
                if line[6] == "_":
                    mtf = line[5]
                else:
                    mtf = line[5:8]
                filename = line[5:].strip("\n")

                if mtf == "A":
                    ca += 1
                elif mtf == "M":
                    cm += 1
                elif mtf == "R":
                    cr += 1
                elif mtf == "P":
                    cp += 1
                elif mtf == "Pab":
                    cpab += 1
                elif mtf == "Pfa":
                    cpfa += 1

            if line[:4] == "RESI":
                    res = line[5:].strip("\n").split(",")

                    for r in range(len(res)):
                        for s in range(len(res)):
                            if r != s:
                                if res[r] == res[s]:
                                    count += 1
                    if count > 0:
                        total.append(filename)

                        if mtf == "A":
                                a += 1
                        elif mtf == "M":
                                m += 1
                        elif mtf == "R":
                                r += 1
                        elif mtf == "P":
                                p += 1
                        elif mtf == "Pab":
                                pab += 1
                        elif mtf == "Pfa":
                                pfa += 1


                # if mtf == "A":
                #     ca += 1
                # elif mtf == "M":
                #     cm += 1
                # elif mtf == "R":
                #     cr += 1
                # elif mtf == "P":
                #     cp += 1
                # elif mtf == "Pab":
                #     cpab += 1
                # elif mtf == "Pfa":
                #     cpfa += 1


            # elif line == "\tmatches = {\n":
            #     flag = True
            #     checkNum = 0
            # elif count > 0 and flag:
            #     total.append((filename, count))
            #     checkNum += 1
            #     count = 0
            # elif flag and count == 0:
            #     checkNum += 1

            #
            # elif flag == True:
            #     if line[:3] == "\t\t'":
            #         if mtf == "A":
            #             a += 1
            #         elif mtf == "M":
            #             m += 1
            #         elif mtf == "R":
            #             r += 1
            #         elif mtf == "P":
            #             p += 1
            #         elif mtf == "Pab":
            #             pab += 1
            #         elif mtf == "Pfa":
            #             pfa += 1
            #         flag = False

    if total != []:
        print "Motifs with Duplicate Residues"
    db = {}
    db["A"] = [ca, ca-a]
    db["M"] = [cm, cm-m]
    db["R"] = [cr, cr-r]
    db["P"] = [cp, cp-p]
    db["Pab"] = [cpab, cpab-pab]
    db["Pfa"] = [cpfa, cpfa-pfa]

    return pd.DataFrame(db, index=["Total", "Nope"]), total


def parsePart3(files):
    for file in files:
        motif = ""
        br = 0

        for line in open(file):
            line = str(line)

            if line[:4] == "FUNC":
                filename = line[5:].strip("\n") + ".py"
            elif line[:4] == "RESI":
                res = line[5:].strip("\n").split(",")
                numRes = sm.comb(len(res),2)
            elif line.strip("\t\n ") == "break":
                br += 1

            if br == 2 and numRes == 1 and len(res) == 2:
                motif += "if flag == False:\n"
                br += 1
            elif br == 3 and numRes == 1 and len(res) == 2 and line != "\n":
                motif += "\t" + line
                br += 1
            elif br == 4 and numRes == 1 and len(res) == 2:
                if line == "\tmatches = {\n":
                    motif += line
                else:
                    temp = line.strip("").split(":")
                    temp2 = temp[0].strip("\t").split("_")
                    motif += "\t\t'" + temp2[0] + "_" + temp2[1] + "' : " + temp[1]
            else:
                motif += line



        if filename == "":
            print "Error: Did not find motif name"
            quit()

        if filename[0] != "J":
            # Writes and adds motif file to new directory
            path = 'Motifs_2.1'
            if not os.path.exists(path):
                os.makedirs(path)
            with open(os.path.join(path, filename), 'wb') as temp_file:
                temp_file.write(motif)
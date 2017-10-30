import scipy.misc as sm
import motifFunctions as cmd
import os
import pandas as pd
global d

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
                    num = int(sm.comb(len(line[5:].split(",")),2))

                    # print filename, "Pos: ", num

                    tot_names = []
                    for aa in res:
                        i = 1
                        string = aa.upper() + str(i)
                        # print "Before while:", string, "list: ",
                        while string in tot_names:
                            string = string.strip(str(i))
                            i += 1
                            string += str(i)
                            # print "Inside while:",
                        tot_names.append(string)

                    res_pairs = []
                    for i in range(len(tot_names)):
                        for j in range(len(tot_names)):
                            if i != j:
                                if (tot_names[i], tot_names[j]) not in res_pairs and (
                                tot_names[j], tot_names[i]) not in res_pairs:
                                    res_pairs.append((tot_names[i], tot_names[j]))
                    if num != len(res_pairs):

                        print "Error: Incorrect number of residue pairs for motif file"
                        raise Warning

            elif line == "'''\n" and flag_info == False:
                motif += line
                flag_info = True


            # Lines that are possible comparisons
            if line[4:10] == "select":
                sele = line.split(",")[1].split("%")
                if len(sele) > 1:

                    if len(sele) != 3:
                        raise Warning
                    try:
                        selection = ((sele[0] + "%" + sele[1]).strip(" '").strip("'")) %float(sele[-1].strip("'(d*").strip("))\n'"))
                    except ValueError:
                        print "Test 15 - Selection Algebra:\n"
                        print "Filename:", filename
                        print sele
                    data = cmd.select(selection=selection, comparisons=comparisons, matrices=mtrx, resPairs = res_pairs)
                    if data == None:
                        pass
                    else:
                        comparisons, mtrx, resPair, flag = data
                        if flag == True:
                            if resPair not in res:
                                if j == len(pairs):
                                    raise Warning
                                pairs[j] = resPair
                                j+=1
                            break
            index += 1

        # Convert Comparison and Distance maps into a map for each residue pair:
        #       - key = "distance"   : value = distance matrix
        #       - key = "comparison" : value = comparison matrix
        motif, newMaps = MaptoString(motif, mtrx, comparisons)


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
    count = 0
    a = 0
    m = 0
    p = 0
    pab = 0
    pfa = 0
    r = 0

    ca = 0
    cm = 0
    cp = 0
    cpab = 0
    cpfa = 0
    cr = 0
    folder = []

    for file in newFiles:

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

            if line == "if flag == False:\n":
                count += 1
                flag = True
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
        if flag == False:
            folder.append(filename)

    db = {}
    db["Fold"] = [len(newFiles), len(newFiles)-count]
    db["A"] = [ca, ca-a]
    db["M"] = [cm, cm-m]
    db["R"] = [cr, cr-r]
    db["P"] = [cp, cp-p]
    db["Pab"] = [cpab, cpab-pab]
    db["Pfa"] = [cpfa, cpfa-pfa]

    print pd.DataFrame(db, index=["Total", "Nope"])
    return folder


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
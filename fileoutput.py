import scipy.misc as sm
import motifFunctions as cmd
import os
import pandas as pd
global d
import copy
import math as m



def MaptoString(motif, distances, comparisons, combo="", newMaps=list()):
    """
    converts maps to file format

    :param motif: file content for current motif
    :param distances: all distances matrices for all pairs in motif OR
                      a distance matrix for a given pair (noted in combo)
    :param comparisons: all comparisons matrices for all pairs in motif OR
                      a comparisons matrix for a given pair (noted in combo)
    :param combo: default -> empty string
                  other   -> residue pair string key for matrices
    :return: updated file content for current motif, list of residue pair string keys
    """

    # Original Parser
    if combo == "":
        newMaps = []

        for pair in distances:

            if pair[0] == pair[1]:
                pass
            else:

                combo = pair[0] + "_" + pair[1]
                newMaps.append(combo)
                motif += combo + \
                                 " = { \n" + "\t'distances'" + ":\n\t\t" + str(distances[pair]) + ",\n"

                motif += "\t'comparisons'" + ":\n\t\t" + str(comparisons[pair]) + "}\n"

    # 3rd Parser
    else:

        newMaps.append(combo)
        motif += combo + " = { \n" + "\t'distances'" + ":\n\t\t" + str(distances) + ",\n"

        motif += "\t'comparisons'" + ":\n\t\t" + str(comparisons) + "}\n"

    return motif, newMaps


def showingResults(filename, num, res, resCombos, comparisons, mtrx):


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

        testIdx = 0

        while False:
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
                                if len(ele) != 5:
                                    print "I am a different size ->", ele
                                skele2.append(ele[2])

                            print "\tRES 2 <", row[0][3], ">", skele2
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
                    allFound = []
                    res = line[5:].strip("\n").split(",")
                    num = m.factorial(len(res))/m.factorial(len(res) - 2)
                    resPairs = []

                    tot = {}
                    for r in res:
                        if r.upper() in tot:
                            tot[r.upper()] += 1
                        else:
                            tot[r.upper()] = 1


                    allHas = {}
                    for nm in tot:
                        val = tot[nm] - 1
                        curr = nm
                        allHas[curr] = [nm]
                        i = "i"
                        for _ in range(val):
                            nm += i
                            allHas[curr].append(nm)
                            i += "i"


                    resCombos = []
                    for i in range(len(res)):
                        for j in range(len(res)):
                            if i != j:
                                combo = (res[i].upper(), res[j].upper(), 0)
                                if combo in resCombos:
                                    if tot[combo[1]] > 1:
                                        pass

                                resCombos.append(combo)

                    if len(resCombos) != num:
                        print "Test: Residue combos list produced incorrectly"
                        print "\tCorrect Number:"
                        print "\tActual Number: ", len(resCombos)
                    copy_combos = copy.deepcopy(resCombos)



                    # if filename == "A_1a65_1_10_3_2":
                    #     print "LIST ->"
                    #     print resCombos
                    #
                    #


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
                    data = cmd.select(name=name.upper(), selection=selection, comparisons=comparisons, matrices=mtrx, resPairs = resPairs, motifname = filename, pairsNeeded=copy_combos, total_names=allFound, total_has=allHas)

                    # Skips extra comparisons
                    if data == None:
                        pass
                    else:
                        comparisons, mtrx, resPairs, allFound = data

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
        showingResults(filename=filename, num=num, res=res, resCombos=resCombos, comparisons=comparisons, mtrx=mtrx)


        if num < len(resPairs):
            motif += "hasExtra = True\n"
            motif += "hasReversed = True\n"

        elif num > len(resPairs):
            # print filename
            # print "-- NUMBER OF RESIDUES --"
            # print "NEEDED -> " + str(num)
            # print "HAVE -> " + str(len(comparisons.keys()))
            #
            # print "-- RESIDUE LIST --"
            # print "NEEDED -> " + str(resCombos)
            # print "HAVE -> " + str(resPairs)
            motif += "hasExtra = False\n"
            motif += "hasReversed = False\n"

        else:
            motif += "hasExtra = False\n"
            motif += "hasReversed = True\n"

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

            print "FILE -> " + file + "\n"

            print "FILENAME -> " + filename + "\n"

            print "MOTIF -> \n\n" + motif + "\n"

            raise Exception("Did not create anything")

        # Source: https://stackoverflow.com/questions/11700593/creating-files-and-directories-via-python

        if filename[0] != "J":
            path = 'C:/Users/Brianna/PyCharmProjects/research/matching-functions/Motifs_old'
            # path = '/home/michael/Documents/Git/bris_research/research/matching-functions-master/Motifs_old'
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
            path = 'C:/Users/Brianna/PyCharmProjects/research/matching-functions/Motifs_2.0'
            # path = '/home/michael/Documents/Git/bris_research/research/matching-functions-master/Motifs_2.0'
            if not os.path.exists(path):
                os.makedirs(path)
            with open(os.path.join(path, filename), 'wb') as temp_file:
                temp_file.write(motif)


def fixingPairStructuresInFiles(motifFile):
    """
    New attempt to fix ill-formed matrices
    """
    extras = []


    # DEFAULTs
    hasReversed = True
    hasExtra = False

    # Initialize
    motif = ""
    # filename = file.lstrip("/home/michael/Documents/Git/bris_research/research/matching-functions-master/Motifs_2.0/").rstrip(".py\n")
    # print filename
    mapsDone = False
    lineIdx = 0
    canBegin = False
    total_pairs = []

    distGo = False
    compGo = False

    for line in open(motifFile):

        print line
        if str(line)[:4] == "FUNC":
            line = str(line)
            filename = line[5:].strip("\n") + ".py"
            print "FILENAME: " + filename + "\n"

        # Before updates
        if not canBegin:
            line = str(line)
            motif += line
            if line == "import motifFunctions as cmd\n":
                canBegin = True
        else:
            # Default cases
            if str(line) == "hasExtra = False\n" or str(line) == "hasReversed = True\n":
                line = str(line)
                motif += line

            # Decides what to do
            elif str(line) == "hasExtra = True\n":
                # Use PCA for extras to determine which to pick
                line = str(line)
                hasExtra = True
                motif += line
            elif str(line) == "hasReversed = False\n":
                # fix ill-produced matrices
                line = str(line)
                hasReversed = False
                motif += line

            # Skip if still at default
            elif hasReversed and not hasExtra:
                motif += line

            # Do stuff now (or later)
            elif not hasReversed and hasExtra or not hasReversed and not hasExtra:

                # Do later
                if hasExtra:
                    extras.append(filename)

                    # Do now including case of both -> add changes for extra later
                if not hasReversed:

                    # Means we've finished all of the maps
                    if str(line) == "flag = False\n":
                        line = str(line)
                        motif += line
                        break

                    elif str(line)[0] != "\t":
                        line = str(line)
                        pair = line.strip(" = { \n")

                        # data = checkMatrix(file, lineIdx, pair, motif)
                        # for due in data[1]:
                        #     total_pairs.append(due)
                        # motif += data[0]


                    elif str(line) == "	'distances':\n":
                        updated_map = {}
                        distGo = True
                        updated_map['distances'] = []

                    elif str(line) == "	'comparisons':\n":
                        compGo = True
                        updated_map['comparisons'] = []

                    elif distGo:
                        line = line.strip().rstrip("\n")
                        distGo = False
                        updated_map['distances'] = line

                        # for i in range(len(line)):
                        #     if i == 0:
                        #         line[i] += "]"
                        #     elif i == len(line) - 1:
                        #         line[i] = "[" + line[i]
                        #     else:
                        #         line[i] = "[" + line[i] + "]"


                    elif compGo:
                        line = line.strip().rstrip("\n")
                        data = cmd.strTomatrix(line, updated_map['distances'])

                        updated_map['comparisons'] = data[0]
                        updated_map['distances'] = data[1]
                        compGo = False
                        motif, total_pairs = checkMatrixHelper(map=updated_map, pair=pair, motif=motif, filename=filename, totPairs=total_pairs)


                        # i = 0
                        # for row in line:
                        #     line[i] = row.split("), (")
                        #     for e in range(len(line[i])):
                        #         # for p in range(len(line[i][e])):
                        #         #     line[i][e] = (line[i][e][0])
                        #         line[i][e] = "(" + line[i][e] + ")"
                        #     i += 1


                        # for i in range(len(line)):
                        #     if i == 0:
                        #         line[i] += ")"
                        #     elif i == len(line) - 1:
                        #         line[i] = "(" + line[i]
                        #     else:
                        #         line[i] = "(" + line[i] + ")"


                else:
                    line = str(line)
                    motif += line

    if not hasReversed and hasExtra or not hasReversed and not hasExtra:
        # Create while loop
        idx = 1
        flag = False
        motif += "while True:\n"
        for pair in total_pairs:
            motif += "\tmatch" + str(idx) + " = " + "cmd.detect(" + str(pair) + ", d, '" + filename + "')\n"

            motif += "\tif match" + str(idx) + " == " + "[]:\n"
            motif += "\t\t flag = True\n"
            motif += "\t\t break\n"
            motif += ""

            if idx == len(total_pairs):
                motif += "\tbreak\n"

            idx +=1

        # Create matches map
        flag = False
        idx = 1
        for pair in total_pairs:
            if len(total_pairs) > 1:
                if flag == False:
                    motif += "\nif flag == False:\n"
                    motif += "\tmatches" + " = " + "{\n\t\t" + pair + ": match" + str(idx) + ","
                    flag = True
                else:
                    if idx < len(total_pairs):
                        motif += "\n\t\t" + pair + ": match" + str(idx) + ","
                    else:
                        motif += "\n\t\t" + pair + ": match" + str(idx) + "}"
            else:

                motif += "\nmatches = {\n\t\t\t" + pair + ": match" + str(idx) + "}"
            idx += 1
        disgard = len("while True:\n")




    lineIdx += 1
    if filename == "":
        raise Exception("Error: Did not find motif name")

    if filename != "J":
        # Writes and adds motif file to new directory
        path = 'C:/Users/Brianna/PyCharmProjects/research/matching-functions/Motifs_3.0'
        # path = '/home/michael/Documents/Git/bris_research/research/matching-functions/Motifs_3.0'
        if not os.path.exists(path):
            os.makedirs(path)
        with open(os.path.join(path, filename), 'wb') as temp_file:
            temp_file.write(motif)




# def checkMatrix(file, index, pair, motif):
#     """
#
#     :param file: current motif file
#     :param index: where to start in the file
#     :param pair: residue pair key for matrix
#     :param motif: motif file content (string)
#     :return:
#     """
#
#     updated_map = {}
#     dist = False
#     comp = False
#     with open(file) as currMotif:
#         for i, line in enumerate(islice(currMotif, index-1, None), index):
#             line = str(line)
#
#             if line[0] != "\t":
#                 return checkMatrixHelper(updated_map, pair)
#             else:
#
#                 # Start analyzing Distance map
#                 if line == "\t'distances':\n":
#                     dist = True
#                     updated_map['distances'] = []
#                 # Start analyzing Comparisons map
#                 elif line == "\t'comparisons':\n":
#                     comp = True
#                     dist = False
#                     updated_map['comparisons'] = []
#
#
#
#
#                 # analyze distances matrix
#                 elif dist:
#
#                     line = line[2:-2].split("), (")
#                     for i in range(len(line)):
#                         if i == 0:
#                             line[i] += ")"
#                         elif i == len(line) - 1:
#                             line[i] = "(" + line[i]
#                         else:
#                             line[i] = "(" + line[i] + ")"
#
#                     updated_map['distances'].append(line)
#
#
#                 # analyze comparisons matrix
#                 # Make into lists
#                 elif comp:
#
#                     line = line[2:-2].split("), (")
#                     for i in range(len(line)):
#                         if i == 0:
#                             line[i] += ")"
#                         elif i == len(line) - 1:
#                             line[i] = "(" + line[i]
#                         else:
#                             line[i] = "(" + line[i] + ")"
#
#                     updated_map['comparisons'].append(line)


def distEqComp(matrix):
    """
    collects sizes of rows in matrix to determine if it is ill-formed

    goal is to compare sizes of maps (distances & comparisons)
    :param matrix: matrix checking
    :return: list of sizes of rows in matrix
    """
    index = 0
    size = 0

    for row in matrix:
        if size == 0:
            size = set()
            size.add(0)
        elif len(row) not in size:
            size.add(index)
        index += 1

    return list(size)


def duploStructures(matrix):
    """
    pre-cond : matrix is comparisons matrix
    :param matrix:
    :return:
    """

    amino = []
    extras = set
    rowIdx = 0
    for row in matrix:
        if row[0][0] in amino:
            extras.add(rowIdx)
        else:
            amino.append(row[0][0])
        rowIdx += 1
    extras = list(extras)
    return extras



def checkMatrixHelper(map, pair, motif, filename, totPairs):
    """
    1. checks if matrices are ill-formed -> if  they are, break them up
    2. converts maps into strings for motif file in proper format
    3. collects all keys that the matrices are mapped to, including new ones produced from breaking up the old
       structures

    :param map: residue pair map
    :param pair: key for matrix
    :param motif: file content for motif (string)
    :param filename: file name for motif
    :param totPairs: totalPairs used in a list
    :return: updated motif content, list of keys for matrices
    """


    sizeComp = distEqComp(map['distances'])
    sizeDist = distEqComp(map['comparisons'])

    test2 = duploStructures(map['comparisons'])

    # try:
    if sizeComp != sizeDist:
        print filename
        print "COMP ->", sizeComp
        print "DIST ->", sizeDist
        print "==================================="
        raise Exception("Distance and Comparison maps have different sizes")

    if test2 != [] or len(sizeComp) > 1 and len(sizeDist) > 1:
        if test2 != [] and len(sizeComp) > 1 and len(sizeDist) > 1:
            # combine lists indices
            return splitMatrices(map, combSizenDuploTests(sizeDist, test2), pair, totPairs)
        elif test2 != []:
            return splitMatrices(map, test2, pair, totPairs)
        elif len(sizeComp) > 1 and len(sizeDist) > 1:
            return splitMatrices(map, sizeDist, pair, totPairs)
    else:
        return MaptoString(motif, map['distances'], map['comparisons'], pair, totPairs)


def combSizenDuploTests(size, duplos):
    """
    Combines results from both tests:
        1. List of indices of a matrix to when a row is a different size
        2. List of indices of a matrix to when a new structure starts (in middle of the matrix)
    :param size:
    :param duplos:
    :return:
    """
    duplos = set(duplos)
    for idx in size:
        duplos.add(idx)
    return list(duplos)




    # except Exception:
    #
    #     print filename
    #     print "COMP ->", sizeComp
    #     print "DIST ->", sizeDist
    #     print "==================================="
    #
    #
    #     getInfo = 0
    #     while True:
    #         cont = raw_input("Do you want more information? ")
    #         if cont == "y":
    #             if getInfo == 0:
    #                 print "Comparisons entire matrix:"
    #                 for row in map['comparisons']:
    #                     print "\t" + str(row)
    #
    #             elif getInfo == 1:
    #                 print "Distances entire matrix:"
    #                 for row in map['distances']:
    #                     print "\t" + str(row)
    #
    #             elif getInfo == 2:
    #                 print "Comparisons rows:"
    #                 for mat in map['comparisons']:
    #                     for row in mat:
    #                         print "\t" + str(row)
    #
    #             elif getInfo == 3:
    #                 print "Distances rows:"
    #                 for mat in map['distances']:
    #                     for row in mat:
    #                         print "\t" + str(row)
    #
    #             else:
    #                 print "No more info"
    #             getInfo += 1
    #
    #         elif cont == "n":
    #             raise Exception("Distance and Comparison maps have different sizes")
    #         else:
    #             print "Only acceptable answers: y - yes & n - no"


def splitMatrices(map, idxList, pair, totPairs):
    """
    breaks matrix up into appropriate matrices then converts into file format & collects all residue pair strings that
    are keys in motif file

    :param map: map holding ill-formed matrices
    :param sizeList: list of sizes and index of where new matrix should begin
    :param pair: residue pair string

    :return: updated file content, list of residue pair string
    """

    start = 0
    motif = ""
    print sizeList

    for m in range(len(idxList)):

        if m == len(idxList) - 1:
            data = MaptoString(motif, map['distances'][start:], map['comparisons'][start:])
            motif += data[0]
            # keys.append(data[1][0])

            # currMap['distances'] = map['distances'][start:]
            # currMap['comparisons'] = map['comparisons'][start:]
            # final.append([pair, currMap])
        else:
            finish = idxList[m+1] + 1

            motif, totPairs = MaptoString(motif, map['distances'][start:finish], map['comparisons'][start:finish], totPairs)
            start = finish - 1
            pair += "i"

            # currMap['distances'] = map['distances'][start:finish]
            # currMap['comparisons'] = map['comparisons'][start:finish]
            # final.append([pair, currMap])


    return motif, totPairs


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
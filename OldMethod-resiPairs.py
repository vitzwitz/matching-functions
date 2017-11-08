import copy
import scipy.misc as sm
import motifFunctions as cmd
"""
Old methods for matrix & map construction involving residue pairs for parsing & rewriting motif files

 - Used data from resi to determine how many residue pairs there were & what they were,
    then adjusted for duplicates
 - Various testing methods to ensure construction was successful
 - From files: fileoutput.py, motifFunctions.py



"""

def inFileOutPut(line):
    """
    figured out how many and what residue pairs there were, then modified the duplicates until
    they were all distinct
    :param line: line in motif
    :return:
    """
    res = line[5:].strip("\n").split(",")
    num = int(sm.comb(len(line[5:].split(",")), 2))

    # print filename, "Pos: ", num

    tot_names = []
    for aa in res:
        string = aa.upper()
        if string not in tot_names:
            tot_names.append(string)
        else:
            while string in tot_names:
                string += "i"

                # print "Inside while:",
            tot_names.append(string)

    res_pairs = []
    for i in range(len(tot_names)):
        for j in range(len(tot_names)):

            if i != j:
                if (tot_names[i], tot_names[j], False) not in res_pairs and (
                tot_names[j], tot_names[i], False) not in res_pairs:
                    res_pairs.append((tot_names[i], tot_names[j], False))

    if num != len(res_pairs):
        print "Number of Residue Pairs: "
        print "\tSHOULD HAVE: ", num
        print "OPTIONS: ", res_pairs
        print "PREV: ", res
        raise Warning
    else:
        resiPairs = copy.deepcopy(res_pairs)


def testsInFileout(resiPairs, comparisons, mtrx, filename, num, res_pairs):
    """
    checked if construction was successful
    :param resiPairs:
    :param comparisons:
    :param mtrx:
    :param filename:
    :param num:
    :param res_pairs:
    :return:
    """
    temp0 = copy.deepcopy(resiPairs)
    temp1 = copy.deepcopy(comparisons)
    temp2 = copy.deepcopy(mtrx)

    comparisons, lst = cmd.updateKeys(comparisons, "C", resiPairs)
    mtrx = cmd.updateKeys(mtrx, "C")

    if len(temp1) != len(comparisons) or len(temp0) != len(resiPairs) or len(temp2) != len(mtrx):
        print "======================================================================================================"
        print "Test 1:\n\tError in update-> Unnecessary deletions (IN FILEOUTPUT.py)"
        print "\t\tImproperly Parsed Motif File: ", filename
        print "\t\t\tNumber of Residues: \n\t\t\t", num

        print "\t\t\tResidue lists: "
        print "\t\t\t\tBefore: \n\t\t\t", temp0
        print "\t\t\t\tAfter: \n\t\t\t", lst

        print "\t\t\tComparisons Maps: "
        print "\t\t\t\tBefore: \n\t\t\t", temp1.keys()
        print "\t\t\t\tAfter: \n\t\t\t", comparisons.keys()

        print "\t\t\tDistance Maps: "
        print "\t\t\t\tBefore: \n\t\t\t", temp2.keys()
        print "\t\t\t\tAfter: \n\t\t\t", mtrx.keys()
        quit()

    data = cmd.checkResults(copy.deepcopy(res_pairs), copy.deepcopy(lst),
                            copy.deepcopy(comparisons), copy.deepcopy(mtrx), \
                            copy.deepcopy(num), copy.deepcopy(filename))
    if data == False:

        quit()
    elif len(data) == 3:
        comparisons, mtrx, passed = data


def checkResults(before,after,comp,dist,num,motifname):
    """
    OLD METHOD IN motifFunctions

    Does various tests to ensure results are appropriate
        pre-conditions : all variables use deep copies

    Tests:

        Assumptions:
        1. len(before) == num
        2. len(after) == num
        3. before == after
        4. Ignoring visited attribute -> before and after have same pairings (and no others)
        5. len(comp) == len(dist)
        6. len(comp) == num and len(dist) == num
        7. comp.keys() == dist.keys() (already in order)
        8. comp.keys() == dist.keys() (after sorting)
        9. len(comp.keys()) == len(before) and len(dist.keys()) == len(before)
        10. Comparison map's keys are all in the residue list after construction

    :param before: original residue pair list
    :param after:  residue pair list returned after completing construction of maps
    :param comp: comparisons map
    :param dist: distance map
    :param num: correct number of pairs
    :param motifname: motiffile name to clarify where the test fails to user
    :return: boolean -> if all tests pass, return true; else, return false
    """
    flag_map = False

    # Res Pair list Tests
    if len(before) != num:
        print "======================================================================================================"
        print "Test 1:\n\tIncorrect number of residue pairs in original list -> SHOULD NOT OCCUR"
        print "\t\tImproperly Parsed Motif File: ", motifname
        print "\t\t\tAfter: \n\t\t\t", before
        print "\t\t\tComp Map: \n\t\t\t", comp.keys()
        print "\t\t\tDist Map: \n\t\t\t", dist.keys()
        return False

    if len(after) != num:
        print "======================================================================================================"
        print "Test 2:\n\tIncorrect number of residue pairs in list after construction -> (Probably changed throughout construction)"
        print "\t\tImproperly Parsed Motif File: ", motifname
        print "\t\t\tNumber of Residues: \n\t\t\t", num
        print "\t\t\tAfter: \n\t\t\t", after
        print "\t\t\tBefore: \n\t\t\t", before
        print "\t\t\tComp Map: \n\t\t\t", comp.keys()
        print "\t\t\tDist Map: \n\t\t\t", dist.keys()
        return False

    if len(before) != len(after):
        print "======================================================================================================"
        print "Test 3:\n\tUnequal number of residue pairs before and after constructing maps"
        print "\t\tImproperly Parsed Motif File: ", motifname
        print "\t\t\tBefore Construction: \n\t\t\t", comp.keys()
        print "\t\t\tAfter Construction: \n\t\t\t", dist.keys()
        return False

    tot_pairs = []
    for aft in after:
        for bef in before:
            if (aft[0], aft[1]) not in tot_pairs:
                if aft[0] == bef[0] and aft[1] == bef[1] or aft[0] == bef[1] and aft[1] == bef[0]:
                    tot_pairs.append((aft[0], aft[1]))
                    break

    if len(tot_pairs) != len(after):
        print "======================================================================================================"
        print "Test 4:\n\tResidue pair lists before and after construction do not match (ignoring order)"
        print "\t\tImproperly Parsed Motif File: ", motifname
        print "\t\t\tBefore Construction: \n\t\t\t", before
        print "\t\t\tAfter Construction: \n\t\t\t", after
        print "\t\t\tTotal Residue Pairs: \n\t\t\t", tot_pairs
        return False


    # Map Tests

    # Check if maps have same number of mappings
    if len(comp) != len(dist):
        print "======================================================================================================"
        print "Test 5:\n\tUnequal number of mappings for two dictionaries"
        print "\t\tImproperly Parsed Motif File: ", motifname
        print "\t\t\tComp Keys: \n\t\t\t", comp.keys()
        print "\t\t\tDist Keys: \n\t\t\t", dist.keys()
        return False

    if len(comp) != num or len(dist) != num:
        print "======================================================================================================"
        print "Test 6:\n\tIncorrect Number of Mappings (Indicated by number possible combinations generated before construction)"
        print "\t\tImproperly Parsed Motif File: ", motifname
        print "\t\t\tAccurate Number of Residues: \n\t\t\t", num
        print "\t\t\tBefore Residue list: \n\t\t\t", before
        print "\t\t\tAfter Residue list: \n\t\t\t", after
        print "\t\t\tComp Keys: \n\t\t\t", comp.keys()
        print "\t\t\tDist Keys: \n\t\t\t", dist.keys()
        return False

    if comp.keys() != dist.keys():
        flag_map = True

    # Put mappings in order
    new_comp = {}
    new_dist = {}

    for key in comp.keys():
        new_comp[key] = comp[key]

        if key not in dist:
            key_temp = (key[1], key[0])
            new_dist[key] = dist[key_temp]
        else:
            new_dist[key] = dist[key]


    if new_comp.keys() != new_dist.keys():
        print "======================================================================================================"
        print "Test 8:\n\tKeys in maps don't match even after re-mapping"
        print "\t\tImproperly Parsed Motif File: ", motifname
        print "\t\t\tComp Keys: \n\t\t\t", new_comp.keys()
        print "\t\t\tDist Keys: \n\t\t\t", new_dist.keys()
        return False

    if len(comp.keys()) != len(before) or len(dist.keys()) != len(before):
        print "======================================================================================================"
        print "Test 9:\n\tOriginal res_pair list and maps' keys have unequal number of pairings "
        print "\t\tImproperly Parsed Motif File: ", motifname
        print "\t\t\tComp Keys: \n\t\t\t", new_comp.keys()
        print "\t\t\tDist Keys: \n\t\t\t", new_dist.keys()
        return False

    upd_pairs = []
    for ky in comp.keys():
        for aft in after:
            if (ky[0], ky[1]) not in upd_pairs:
                if ky[0] == aft[0] and ky[1] == aft[1] or ky[0] == aft[1] and ky[1] == aft[0]:
                    upd_pairs.append((ky[0], ky[1]))
                    break

    if upd_pairs != comp.keys():
        print "======================================================================================================"
        print "Test 10:\n\tComparison map's keys are all in the residue list after construction"
        print "\t\tImproperly Parsed Motif File: ", motifname
        print "\t\tAfter Construction: \n\t", after
        print "\t\tComp Keys: \n\t\t\t", new_comp.keys()
        print "\t\tDist Keys: \n\t\t\t", new_dist.keys()
        print "\t\tTotal Residue Pairs: \n\t\t\t", upd_pairs
        return False

    # Passes all tests
    if flag_map == True:
        return new_comp, new_dist, True
    else:
        return True

def modifyName(res, pair):
    "How many I's? in residue"
    eye = ""
    flag = False

    ra = pair[0][:len(pair[0]) - 1]
    rb = pair[1][:len(pair[1]) - 1]

    # for i in range(len(res) - 1, -1, -1):
    #
    #     if ra + eye == res:
    #         return ra + eye + pair[0][len(pair[0]) - 1], 0
    #     elif rb + eye == res:
    #         return rb + eye + pair[1][len(pair[1]) - 1], 1
    #
    #     elif res[i] == "I" and flag == False:
    #         eye += res[i]
    #
    #     elif res[i] != "I":
    #         break

    r1 = pair[0][:len(pair[0]) - 1] #+ eye
    r2 = pair[1][:len(pair[1]) - 1] #+ eye

    return r1, r2

def buildKey(res1,res2,resPairs):
    """
    OLD METHOD IN motifFunctions

    Builds key for matrix dictionaries -> accounts for duplicate residues in
    :param res1: res name 1
    :param res2: res name 2
    :param resPairs: list of possible residues for motif file
    :return: tuple containing names of residue 1 and 2 with index
    """
    # print "Res 1: ", res1
    # print "Res 2: ", res2

    # Test cases:
    if res1[-1] != "i" and len(res1) > 3:
        print "What is res1? ", res1
    if res2[-1] != "i" and len(res1) > 3:
        print "What is res2?", res2

    hasI = False
    for comp in resPairs:
        if comp[0][-1] == "i" or comp[1][-1] == "i":
            hasI = True
            break


    for p in range(len(resPairs)):

        r1, r2, flag = resPairs[p]
        if flag == False:

            if hasI:
                # data1 = modifyName(res1, pair)
                # data2 = modifyName(res2, pair)

                # if isinstance(data1[1], str) and isinstance(data2[1], str):

                # print "============= IN BUILD KEY =============="
                # print "All options"
                if (res1 == r1 and res2 == r2):

                    # print "In selection algebra"
                    # print res1
                    # print res2
                    #
                    # print "In res pairs: "
                    # print r1
                    # print r2

                    return (r1, r2, flag)
                elif (res1 == r2 and res2 == r1):

                    # print "In selection algebra"
                    # print res1
                    # print res2
                    #
                    # print "In res pairs: "
                    # print r2
                    # print r1
                    del resPairs[p]
                    if p == len(resPairs):
                        resPairs.append((r2, r1, flag))
                    else:
                        resPairs[p] = (r2, r1, flag)

            else:
                r1 = copy.deepcopy(r1).strip("i")
                r2 = copy.deepcopy(r2).strip("i")
                if res1 == r1 and res2 == r2:

                    # print "In selection algebra"
                    # print res1
                    # print res2
                    #
                    # print "In res pairs: "
                    # print r1
                    # print r2

                    return (r1, r2, flag)
                elif res1 == r2 and res2 == r1:

                    # print "In selection algebra"
                    # print res1
                    # print res2
                    #
                    # print "In res pairs: "
                    # print r2
                    # print r1
                    del resPairs[p]
                    if p == len(resPairs):
                        resPairs.append((r2, r1, flag))
                    else:
                        resPairs[p] = (r2, r1, flag)
                    return (r2, r1, flag)


            # elif isinstance(data1[1], str):
            #     r11, r21 = data1
            #     r2 = data2[0]
            #
            #     if data2[1] == 0:
            #         if res1 == r21 and res2 == r2:
            #             r1 = r21 + pair[1][len(pair[1]) - 1]
            #             return (r1, r2)
            #
            #     elif data2[1] == 1:
            #         if res1 == r11 and res2 == r2:
            #             r1 = r11 + pair[0][len(pair[0]) - 1]
            #             return (r1, r2)
            #
            # elif isinstance(data2[1], str):
            #     r1 = data1[0]
            #     r12, r22 = data2
            #
            #     if data1[1] == 0:
            #         if res1 == r1 and res2 == r22:
            #             r2 = r22 + pair[1][len(pair[1]) - 1]
            #             return (r1, r2)
            #
            #     elif data2[1] == 1:
            #         if res1 == r1 and res2 == r12:
            #             r2 = r12 + pair[0][len(pair[0]) - 1]
            #             return (r1, r2)
            # else:
            #     return (data1[0], data2[0])

    # d = {}
    # d["[R1_O1]"] = res1_op1
    # d["[R1_O2]"] = res1_op2
    # d["[R2_O1]"] = res2_op1
    # d["[R2_O2]"] = res2_op2
    # table(d, res1, res2, resPairs)
    return


def table(d, res1, res2, lst):

    # tbl = pd.DataFrame(d)
    print "============ IN TABLE -> COULDN'T FIND MATCH ============="
    print "Residues: ", (res1, res2)
    print "From Motif: ", lst
    # print tbl
    quit()

def updateKeys(map, status, lst=list()):
    """
    OLD METHOD IN motifFunctions

    pre-condition: all keys in map exist in resPairs

    updates all keys in maps and tuples in list to visited
    :param map: dictionary to be updated
    :param lst: list of tuples to be updated
    :param status: status of building all maps for file
            "I" - incomplete -> has to ignore certain cases
            "C" - complete -> removes visited parameter for all cases
    :return: updated map, updated residue pair list
    """


    use = False
    for ky in map:

        if status == "I":
            if ky[2] == False:

                # New key
                key = (ky[0], ky[1], True)

                if lst != []:
                    # Update reside pair list
                    # print "============== IN UPDATE ==================="
                    for e in range(len(lst)):
                        if lst[e] == ky:

                            # Update list
                            del lst[e]
                            if e == len(lst) - 1:
                                lst.append(key)
                            else:
                                lst.insert(e, key)

                            # Old value
                            val = map[ky]

                            # Delete old mapping
                            del map[ky]

                            # Update
                            map[key] = val

                            # Set use flag to true -> continue after this update
                            use = True
                            break
                else:

                    # Old value
                    val = map[ky]

                    # Delete old mapping
                    del map[ky]

                    # Update
                    map[key] = val
        elif status == "C":
             if len(ky) == 3:

                # Removes visited parameter of element
                key = (ky[0], ky[1])

                if lst != []:
                    # Update list
                    for e in range(len(lst)):
                        if lst[e][0] == ky[0] and lst[e][1] == ky[1]:

                            # Update list
                            del lst[e]
                            if e == len(lst) - 1:
                                lst.append(key)
                            else:
                                lst.insert(e, key)

                            # Old value
                            val = map[ky]

                            # Delete old mapping
                            del map[ky]

                            # Update
                            map[key] = val
                            break

                        elif lst[e][0] == ky[1] and lst[e][1] == ky[0]:

                            key = (ky[1], ky[0])
                            # Update list
                            del lst[e]
                            if e == len(lst) - 1:
                                lst.append(key)
                            else:
                                lst.insert(e, key)


                            # Old value
                            val = map[ky]

                            # Delete old mapping
                            del map[ky]

                            # Update
                            map[key] = val
                            break
                else:
                    # Old value
                    val = map[ky]

                    # Delete old mapping
                    del map[ky]

                    # Update
                    map[key] = val

    if status == "I":
        if lst != [] and use == True:
            return map, lst
        elif lst == []:
            return map
        else:
            return
    elif status == "C":
        if lst != []:
            return map, lst
        else:
            return map


def checkBuildDicts(comparisons, matrices, resPairs, resComp, motifname):
    """
    OLD CHECK INSIDE builddict IN motifFunctions.py
    :param comparisons: map with pair names mapping to matrices with elements consisting of
            atom names, residue names, & distances
    :param matrices: map with pair names mapping to matrices with elements consisting of
            distances
    :param resPairs: 1D graph of possible residue pairs for motifs
    :param resComp: residue combo (single pair)
    :param motifname: name of motif being built
    :return:
    """
    if len(comparisons) > 0:
        if comparisons.keys() != matrices.keys():
            print "=================================================================================\n\t"
            print "Test 1: (In build dict)"
            print "\n\t\tMotif: ", motifname
            print "\n\t\t\tRES - PAIRS -> ", resPairs
            print "\n\t\t\tRES COMBO -> ", resComp
            quit()

        temp1 = copy.deepcopy(resPairs)
        temp2 = copy.deepcopy(comparisons)

        # Updated finished matrices to visited
        data_comp = updateKeys(comparisons, "I", resPairs)

        # Already used
        if data_comp == None:
            return

        comparisons, resPairs = data_comp
        matrices = updateKeys(matrices, "I")

        if len(resPairs) != len(temp1) or len(comparisons) != len(temp2):
            print "====================================================================================\n"
            print "Test 2: (In build dict)"
            print "\tMotifname: \n\t\t", motifname
            print "\t\tRes Lists:"
            print "\t\t\tBefore-> \n\t\t\t\t", temp1
            print "\t\t\tAfter-> \n\t\t\t\t", resPairs

            print "\t\tComparison Map: "
            print "\t\t\tBefore-> \n\t\t\t\t", temp2
            print "\t\t\tAfter-> \n\t\t\t\t", comparisons
            quit()
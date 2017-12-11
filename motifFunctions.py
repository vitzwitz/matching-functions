import config
import time as t
import numpy as np
import numpy.linalg as nl
import pandas as pd
import scipy.stats as st
import os
# import mysql.connector
import pandas as pd
import copy

class Cluster(object):
    def __init__(self, atom1, atom2, res1, res2, r, id):
        self.atom1 = str(atom1)
        self.atom2 = atom2
        self.res1 = str(res1)
        self.res2 = str(res2)
        self.dist = r
        self.id = id

    def __str__(self):
        return "Cluster " + str(id) + ": <" + self.atom1 + " in " + self.res1 + " n. " + str(self.atom2) + " in " + self.res2 +">"

def storeData(match, res1, res2, totalTime, motifName, i):
    # Initialize map for storing data
    atomMap = {}
    firstpdb = match.keys()[0]

    atom1 = match[firstpdb][0][0]
    atom2 = []
    for a in match[firstpdb][1]:
        atom2.append(a[0])


    key = res1 + "_" + atom1
    atomMap[key] = {"name": [], "res": [], "chainID": [], "x": [], "y": [], "z": [], "occupancy": [],
                      "tempFact": [], "time": []}
    for atm in atom2:
        key = res2 + "_" + atm
        atomMap[key] = {"name": [], "res": [], "chainID": [], "x": [], "y": [], "z": [], "occupancy": [],
                        "tempFact": [], "time": []}
    for pdb in match:
        atomMap = storeDataHelper(atom1,atom2,res1,res2,match,pdb,atomMap,totalTime)

    # Build Tables for each atom
    path_data = 'C:/Users/Brianna/PyCharmProjects/optimizer/Data/' + motifName + '/'
    if not os.path.exists(path_data):
        os.makedirs(path_data)

    for atom_res in atomMap:
        file = path_data + atom_res + str(i)
        # print atomMap[atom_res]
        atom = pd.DataFrame(atomMap[atom_res], index=match.keys())#.to_sql(name=str(atom), flavor='mysql')

        # Send to Database here when MySQL is connected & understood
        atom.to_pickle(file)

        # Use line while testing tables
        # pd.read_pickle(file)


def storeDataHelper(atom1,atom2, res1,res2, match, pdb, atomMap, TOTtime):
    key = res1 + "_" + match[pdb][0][0]
    atomMap[key] = getAtomAttr(atom=config.TREEs[pdb].data[match[pdb][0][1]], atomMap=atomMap[key],
                               name=atom1, res=res1, time=TOTtime)

    for pair in match[pdb][1]:
        key = res2 + "_" + pair[0]
        atomMap[key] = getAtomAttr(atom=config.TREEs[pdb].data[pair[1]], atomMap=atomMap[key], name=atom2, res=res2,
                                   time=TOTtime)
    return atomMap


# def match(name, matches, r, res1, atom1, res2, atoms):
#     before = t.time()
#     matches[name] = config.TREEs.query_pairs(r=r, res1=res1, atomName1=atom1, res2=res2, atomName2=atoms)
#     # print("Match: ", name, t.time() - before)
#     if matches[name] == list():
#         matches = {}
#         print "Motif failed!"
#         quit()

def matchEach(r, res1, atom1, res2, atom2, motifName, i):

    # Initialize map for resulting matches for this cluster
    match = {}


    for pdb in config.TREEs:
        startTime = t.time()
        # print "atom 1: " + atom1
        # print "atom 2: " + str(atom2)
        # print "atom 1: " + res1
        # print "atom 2: " + res2

        match[pdb] = config.TREEs[pdb].query_pairs(r=r, res1=res1, atomName1=atom1, res2=res2, atomName2=atom2)

        if match[pdb] == list():
            print "Motif failed!", motifName
            return

        TOTtime = t.time() - startTime
        # Match ex : [48, [('C', 6), ('CG', 8), ('CG', 74), ('N', 4), ('OD1', 9), ('O', 3), ('ND2', 8)]]

    return match, TOTtime


def getAtomAttr(atom, atomMap, name, res, time):
    """
    getAtomAttr stores the atom's data

    post - condition : all data stored will be a number (int or float)

    name (int)            : name == name from motif
    res (int)             : res name == res name from motif
    chain (int)           : ord(chain ID) - 64
                                A = 1, B = 2, ...
    x (float)             : x-coordinate
    y (float)             : y-coordinate
    z (float)             : z-coordinate
    occupancy (float)     : occupancy
    tempFact (float)      : temperature factor
    time (float)          : total time of search for cluster


    :param atom: atom to get attributes from
    :param atomMap: map to store data
    :param name: list of atoms from motif constraint
    :param res: string residue name from motif constraint
    :param time: float time for search
    :return: updated map
    """
    if atom.name in name:
        atomMap["name"].append(1)
    else:
        atomMap["name"].append(0)

    if atom.resName == res:
        atomMap["res"].append(1)
    else:
        atomMap["res"].append(0)
    atomMap["chainID"].append(ord(atom.chainID)-64)
    atomMap["x"].append(atom.x)
    atomMap["y"].append(atom.y)
    atomMap["z"].append(atom.z)
    atomMap["occupancy"].append(atom.occupancy)
    atomMap["tempFact"].append(atom.tempFact)
    atomMap["time"].append(time)
    return atomMap


        # path = 'Motifs'
        # filename = pdb + '.py'
        # if not os.path.exists(path):
        #     os.makedirs(path)
        #
        # with open(os.path.join(path, filename), 'wb') as temp_file:
        #     temp_file.write(motif)

def testConstruction(map, numPairs, pairs):
    return checkSize(map), checkNames(numPairs=numPairs, map=map, pairs=pairs)



def moreTests(combos, map, res, num):
    results = ""
    results += "DESIRED ->\n"
    results += "\t" + str(combos) + "\n"
    results += "ACTUAL ->\n"
    results += "\t" + str(map.keys()) + "\n\n"

    results += "In Data (TOP of motif file) ->\n"
    results += "\t" + str(res) + "\n"
    results += "Desired Num Pairs ->\n"
    results += "\t" + str(num)

    return results





def checkNames(map, numPairs, pairs):
    """
    compare the keys in the map with the elements in the pairs list
        Checks if :
            - Too little residue comparisons (matrices) produced in maps
            - Map uses all possible pairs in list
    :param map: map that maps residue pairs to data matrices
    :param numPairs: minimum number of residue pairs
    :param pairs: list of residue pairs
    :return: boolean regarding success 1st test, list of possible missing residue pairs
    """
    problem = False
    missing = []
    extra = []
    results = ""


    # Produced too little matrices -> too little residue pairs compared
    if len(map) < numPairs:
        results += "\tB. Too little total residue pairs in motif\n"
        results += "\t\tDesired Num Pairs -> " + str(numPairs) + "\n"
        problem = True

    for ky in map:
        idx = -2
        found = False
        for p in range(len(pairs)):
            if ky[0] == pairs[p][0] and ky[1] == pairs[p][1] and pairs[p][2] == 0:

                new = (pairs[p][0], pairs[p][1], pairs[p][2] + 1)
                del pairs[p]
                if p == len(pairs):
                    pairs.append(new)
                else:
                    pairs[p] = new
                found = True
                break

            elif ky[0] == pairs[p][0] and ky[1] == pairs[p][1] and pairs[p][2] > 0:
                idx = p

        if idx != -2 and not found:

            new = (pairs[idx][0], pairs[idx][1], pairs[idx][2] + 1)
            del pairs[idx]
            if idx == len(pairs):
                pairs.append(new)
            else:
                pairs[idx] = new


    results += "\tC. Missing/Extra Residue Pairs \n\n"
    results += "\t\tDesired Total Needed Num Pairs -> " + str(numPairs) + "\n"
    results += "\t\tActual Total Needed Num Pairs -> " + str(len(map.keys())) + "\n"
    results += "\t\tResults inside map -> " + str(map.keys()) + "\n"
    results += "\t\tResults inside pair list ->" + str(pairs) + "\n"

    x = 0
    m = 0
    for pair in pairs:
        if pair[2] == 0:
            if problem == False:
                problem = True
            missing.append((pair[0], pair[1]))

            m += 1
            results += "\t\t\tMissing Pairs " + str(m) + "\n"
            results += "\t\t\t-> " + pair[0] + " & " + pair[1] + "\n"

        # elif pair[2] > 1:
        #     if problem == False:
        #         problem = True
        #     extra.append((pair[0], pair[1]))
        #
        #     x += 1
        #     results += "\t\t\tExtra Pair (Duplicates) " + str(x) + " \n"
        #     results += "\t\t\t-> " + pair[0] + " & " + pair[1] + "\n"

    if missing == [] and extra == [] and not problem:
        return problem, ""
    elif missing == [] and extra == [] and problem:
        return problem, "\tB. Too little total residue pairs in motif\n" \
                            "\t\tDesired Num Pairs -> " + str(numPairs) + "\n" \
                            "\t\tActual Num Pairs -> " + str(len(map)) + "\n"

    else:
        return problem, results


def checkSize(map):
    """
    Calculates the size of the rows for each matrix in the map,
    then builds a string that consists of the results from this test

    pre-condition: map -> maps to a list or list of lists

    :param map: map that's being looked at
    :return: map of the results for each mapping in the given map
    """

    results = ""
    hasProb = False
    for mtrx in map:
        rowSz = []
        for row in mtrx:
            if rowSz == []:
                rowSz.append(len(row))
            elif len(row) not in rowSz:
                rowSz.append(len(row))
        if len(rowSz) != 1:
            if hasProb == False:
                hasProb = True

            results += "\tA. Row Size Changes for Res Pair: " + str(mtrx) + "\n"
            results += "\t\tSHOULD BE-> " + str(rowSz[0]) + "\n"
            for sz in rowSz:
                results += "\t\t\tGOT -> " + str(sz) + "\n"

    return hasProb, results




def select(name, matrices, comparisons, selection, resPairs, motifname, pairsNeeded, total_names, total_has):
    """

    :param matrices: distance matrix
    :param comparisons: matrix of comparison objects
    :param selection: selection algebra
    :param resPairs: all possible res pairs in motif file

    :return: updated matrices
    """



    a = 0
    resComp = ()
    sele = selection.split()

    if name not in total_names:
        total_names.append(name)

    for pie in sele:
        if pie == 'n.' or pie == "'n.":
            a += 1
        elif a == 1:
            if pie[-3:] == '&r.':
                atom1 = pie.strip('&r.')
            else:
                try:
                    r = float(pie)
                except:
                    if pie != 'w.' and pie != 'of':
                        res1 = pie.upper()
        elif a == 2:
            if "&" in pie:
                if pie[-3:] == '&r.':
                    atom2 = pie.strip('&r.')
                else:
                    second = pie.split("&")
                    atom2 = second[0]
                    res2 = second[1].upper()
                    # print "============= IN SELECT (Parser) =============="
                    # print "Res in selection alg: ", res1, res2
                    # print "Res Combo: ", resComp


                    if name != res1:
                        resComp = (name, res2)

                    elif res1 == res2 and name == res1:
                        resComp = (res1, res2 + "I")
                    else:
                        resComp = (res1, res2)
            else:
                if pie != 'w.' and pie != 'of':
                    res2 = pie.upper()

                    if name != res1:
                        resComp = (name, res2)
                    else:
                        resComp = (res1, res2)
    try:
        if resComp == () or atom1 == "" or atom2 == "" or res1 == "" or res2 == "":
            raise Exception("Select failed: Did not collect all necessary data")
    except:
        raise Exception("Select failed: Did not find all needed atoms and residues")

    # Build list of matches
    buildDicts(resComp=resComp, comparisons=comparisons, matrices=matrices, atom1=atom1, atom2=atom2, res1=res1, res2=res2, r=r, resPairs=resPairs, motifname=motifname, pairsNeeded=pairsNeeded, names=total_names, allHas=total_has)

def strTomatrix(matCom, matDist):

    isComp = False
    isDist = False
    dist = []
    comp = []
    # how to handle distances matrix
    matDist = matDist.split(",")

    for e in matDist:
        e = e.strip()

        if e != "":
            if e[0] == "[":
                if len(e) >= 2 and e[:3] == "[[(" or e[-1] == "]":
                    # start of matrix OR entire row (rows with one element)
                    dist.append([float(e.lstrip("[").rstrip("]"))])
                elif e[-1] != "]":
                    # start of row with more than one element (NOT FIRST)
                    dist.append([float(e.lstrip("[").rstrip("]"))])

                elif len(e) >= 2 and e[:2] == "[[" or e[-1] == "]":
                    # start of matrix OR entire row (rows with one element)
                    dist.append([float(e.lstrip("[").rstrip("]"))])
                elif e[-1] != "]":
                    # start of row with more than one element
                    dist.append([float(e.lstrip("[").rstrip("]"))])

            elif e[0] != "[":
                # inside matrix
                if type(dist[-1]) == list:
                    if type(dist[-1][-1]) == list:
                        dist[-1][-1].append(float(e.lstrip("[").rstrip("]")))
                    elif type(dist[-1][-1]) == float:
                        dist[-1].append(float(e.lstrip("[").rstrip("]")))

            else:
                if type(dist[-1]) == list:
                    if type(dist[-1][-1]) == list:
                        dist[-1][-1].append(e)
                    elif type(dist[-1][-1]) == float:
                        dist.append(e)

    # how to handle comparisons matrix
    matCom = matCom.split("], [")

    for e in matCom:
        ele = []
        e = e.split("), (")

        for strEle in e:
            strEle = strEle.split(",")
            strEle[0] = strEle[0].strip("\t")
            # print "<" + strEle[0] + ">"
            # print
            if strEle[0][:4] == "[[('" or strEle[0][0] == "(" or strEle[0][:2] == "[(":
                if strEle[0][:4] == "[[('":
                    atm1 = strEle[0].lstrip("[[('").rstrip("'")
                    rs1 = strEle[1].lstrip(" '").rstrip("'")
                    atm2 = strEle[2].lstrip(" '").rstrip("'")
                    rs2 = strEle[3].lstrip(" '").rstrip("'")

                    if strEle[4][-1] == ")":
                        dst = strEle[4].lstrip().rstrip(")")
                    else:
                        dst = strEle[4].strip()
                    ele.append((atm1, rs1, atm2, rs2, float(dst)))

                elif strEle[0][:2] == "[(":
                    atm1 = strEle[0].lstrip("[('").rstrip("'")
                    rs1 = strEle[1].lstrip(" '").rstrip("'")
                    atm2 = strEle[2].lstrip(" '").rstrip("'")
                    rs2 = strEle[3].lstrip(" '").rstrip("'")
                    if strEle[-1][-3:] == ")]}":
                        dst = strEle[4].strip(")]}")
                    else:
                        dst = strEle[4].strip()

                    ele.append((atm1, rs1, atm2, rs2, float(dst)))
                else:
                    atm1 = strEle[0].lstrip("('").rstrip("'")
                    rs1 = strEle[1].lstrip(" '").rstrip("'")
                    atm2 = strEle[2].lstrip(" '").rstrip("'")
                    rs2 = strEle[3].lstrip(" '").rstrip("'")

                    if strEle[4][-1] == ")":
                        dst = strEle[4].rstrip(")")
                    elif strEle[4][-4:] == ")]]}":
                        dst = strEle[4].rstrip(")]]}")
                    else:
                        dst = strEle[4].strip()
                    ele.append((atm1, rs1, atm2, rs2, float(dst)))

            else:

                if strEle[-1][-4:] == ")]]}":
                    atm1 = strEle[0].lstrip("[[('").rstrip("'")
                    rs1 = strEle[1].lstrip(" '").rstrip("'")
                    atm2 = strEle[2].lstrip(" '").rstrip("'")
                    rs2 = strEle[3].lstrip(" '").rstrip("'")
                    dst = strEle[4].lstrip().rstrip(")]]}")

                    ele.append((atm1, rs1, atm2, rs2, float(dst)))
                elif strEle[-1][-3:] == ")]}":
                    atm1 = strEle[0].lstrip("[[('").rstrip("'")
                    rs1 = strEle[1].lstrip(" '").rstrip("'")
                    atm2 = strEle[2].lstrip(" '").rstrip("'")
                    rs2 = strEle[3].lstrip(" '").rstrip("'")
                    dst = strEle[4].lstrip().rstrip(")]}")

                    ele.append((atm1, rs1, atm2, rs2, float(dst)))

                    # return comp, dist
                else:
                    atm1 = strEle[0].lstrip("'").rstrip("'")
                    rs1 = strEle[1].lstrip(" '").rstrip("'")
                    atm2 = strEle[2].lstrip(" '").rstrip("'")
                    rs2 = strEle[3].lstrip(" '").rstrip("'")
                    dst = strEle[4].lstrip().rstrip(")")
                    dst = strEle[4].strip(")]")

                    ele.append((atm1, rs1, atm2, rs2, float(dst)))

        comp.append(ele)

    return comp, dist

def printMatrix(mat):

    print "matrix ="
    for row in mat:
        print "\t" + str(row)

def buildDicts(resComp, comparisons, matrices, atom1, res1, atom2, res2, r, resPairs, motifname, pairsNeeded, names, allHas):
    """
    builds current line from current motif onto comparisons dictionary (comparisons)
    and distance dictionary (matrices)

    post-condition : each element in each value in comparisons (dictionary) consists of a tuple in this exact order:
                        element = (atom1, res1, atom2, res2, r)
                     If update is successful with the map comparisons, it will be successful with the map matrices
                     If comparisons is empty, matrices is empty and if comparisons has an mapping, matrices has a mapping

    :param resComp: pair of residue names
    :param comparisons: dictionary of matrices of atoms to compare
    :param matrices: dictionary of distance matrices
    :param atom1: atom name for current row that's being built 
    :param res1: residue name for current matrix that's being built
    :param atom2: atom name for element that's being built in comparisons
    :param res2: residue name for current matrix that's being built in comparisons
    :param r: distance for current element that's being built in matrices
    :return: matrix dictionaries, key to value updated, boolean
    """

    # If current residue pair is different from the last residue pair added to the list, it means it's a new pair



    if resPairs == [] or resComp != resPairs[-1] or resComp not in resPairs:

        # print "CURR_ELE[i] =", resComp
        # print "CURR_COLLECTED[i] =", names
        # print "NEEDS[i] =", allHas
        # print "HAS[i] =", resPairs
        # print "i+=1"
        # print "'======================================='\n"



        if (resComp[0], resComp[1]) in resPairs:
            for name in names:
                if name.strip("I") == resComp[1] and len(name) != len(resComp[1]):
                    resComp = (resComp[0], name)
                    break
            if (resComp[0], resComp[1]) != resComp:
                print "COMBO MADE:", resComp, "\nCURR NAME:", name, "\nTOT NAMES:", allHas

        # found = False
        # # Find unused pair that matches
        # for p in range(len(pairsNeeded)):
        #
        #         if pairsNeeded[p][0] == resComp[0] and pairsNeeded[p][1] == resComp[1]:
        #             if pairsNeeded[p][2] == 0:
        #
        #
        #
        #
        #                 resComp = (pairsNeeded[p][0], pairsNeeded[p][1])
        #
        #                 pair = (pairsNeeded[p][0], pairsNeeded[p][1], 1)
        #                 pairsNeeded[p] = pair
        #                 found = True
        #                 break
        #             else:
        #
                # elif pairsNeeded[p][0] == resComp[0].strip("I") and pairsNeeded[p][1] == resComp[1].strip("I"):
                #     if pairsNeeded[p][2] == 0:
                #
                #         resComp = (pairsNeeded[p][0], pairsNeeded[p][1] + ext)
                #
                #         pair = (pairsNeeded[p][0], pairsNeeded[p][1] + ext, 1)
                #         pairsNeeded[p] = pair
                #         found = True
                #         break
                #     else:
                #         ext += "I"

        # Add to used list of residue pairs
        resPairs.append(resComp)

        # Add to map
        matrices[resComp] = [r]
        comparisons[resComp] = [(atom1, res1, atom2, res2, r)]






    elif type(comparisons[resComp][-1]) == list:
        if comparisons[resComp][-1][-1][1] != res1 or comparisons[resComp][-1][-1][3] != res2:
            # Make new matrix
            print "============= IN BUILD DICTIONARY =============="
            print "Res1 in cluster: ", comparisons[resComp][-1][-1][1]
            print "Res2 in cluster: ", comparisons[resComp][-1][-1][3]

            print "Res1: ", res1
            print "Res2: ", res2
            raise Exception("BuildDict failed: Current residues do not match residues in current map that is being built")

        elif comparisons[resComp][-1][-1][0] == atom1:
            comparisons[resComp][-1].append((atom1, res1, atom2, res2, r))
            matrices[resComp][-1].append(r)
        else:
            comparisons[resComp].append([(atom1, res1, atom2, res2, r)])
            matrices[resComp].append([r])

    elif isinstance(comparisons[resComp][-1], tuple):
        if comparisons[resComp][-1][0] == atom1:
            comparisons[resComp].append((atom1, res1, atom2, res2, r))
            matrices[resComp].append(r)
        else:
            comparisons[resComp] = [comparisons[resComp], [(atom1, res1, atom2, res2, r)]]
            matrices[resComp] = [matrices[resComp], [r]]

    else:
        raise Exception("Error: Dictionary should contain Match objects / Lists of Match objects / List of lists of Match objects")

    return comparisons, matrices, resPairs, names



def covariance(mtrx):
    """
    Build covariance matrix from given matrix
        Steps:
                1. Find the average of the columns
                2. Subtract the average column from the matrix
                3. Take the transpose of the result from number 2
                4. Take the dot product of the results from 2 and 3

    Citation : http://www.cs.toronto.edu/~guerzhoy/320/lec/pca.pdf
               http://www.vision.jhu.edu/teaching/vision08/Handouts/case_study_pca1.pdf
    :param mtrx: matrix
    :return: covariance matrix of given matrix
    """

    # Average column of matrix
    T = np.transpose(mtrx)
    ave = np.zeros(len(mtrx))
    mtrx = np.asarray(mtrx)

    if isinstance(mtrx, np.ndarray):
        ave = average(T)

    for col in T:
        if type(mtrx) == list:
            # If data isn't standardized
            ave += np.asarray(col)


    if len(mtrx[0]) > len(mtrx):
        for moreRows in range(len(mtrx[0]), len(mtrx)):
            mtrx[moreRows] = np.asarray(mtrx[moreRows])

    ave /= len(mtrx[0])


    phi = T - ave
    # Covariance matrix
    return np.dot(np.transpose(phi), phi)


def squaringMatrices(mtrx):
    dof = len(mtrx) - len(mtrx[0])

    if dof < 0:
        print "dim(C) > dim(R)"

        if isinstance(mtrx, list):
            zeros = []
            for lstZr in range(len(mtrx[0])):
                zeros.append(0.0)
            for nwrw in range(abs(dof)):
                mtrx.append(zeros)

        elif isinstance(mtrx, np.ndarray):
            zeros = np.zeros((abs(dof), len(mtrx[0])))
            mtrx = np.append(mtrx, zeros, axis=0)

    elif dof > 0:
        print "dim(C) < dim(R)"

        if isinstance(mtrx, list):
            for row in mtrx:
                for zr in range(abs(dof)):
                    row.append(0.0)
        elif isinstance(mtrx, np.ndarray):
            zeros = np.zeros((len(mtrx), abs(dof)))
            mtrx = np.append(mtrx, zeros, axis=1)

            # stand = st.zscore(mtrx, axis=0, ddof=abs(dof))

    else:
        print "dim(C) == dim(R)"
    return mtrx


def average(array):
    ave = 0
    if isinstance(array, np.ndarray) or isinstance(array, list):
        if isinstance(array[0], np.ndarray):
            for e in array:
                ave += e
            ave /= len(array[0])
        elif isinstance(array[0], list):
            for e in array:
                ave += np.asarray(e)
                ave /= len(array[0])
        else:
            for e in array:
                ave += e
            ave /= len(array)
    return ave


def scale(data):
    # https://docs.tibco.com/pub/spotfire/7.0.0/doc/html/norm/norm_scale_between_0_and_1.htm
    scaled = []
    min = np.min(data)
    max = np.max(data)

    for eig in data:
        scaled.append((eig - min) / (max - min))

    return np.asarray(scaled)

# def mean(mtrx):
#     if len(mtrx) == len(mtrx[0]):
#         return np.mean(mtrx)
#     else:
#         mean = 0
#         for row in mtrx:
#             for ele in row:
#                 mean+=ele

def pca(mtrx):
    """
    Citation :
        1. Method for standardizing data:
            i. Numpy
            ii. https://stackoverflow.com/questions/4544292/how-do-i-standardize-a-matrix
        2. PCA overall:
            i. iii. https://www.researchgate.net/post/What_is_the_best_way_to_scale_parameters_before_running_a_Principal_Component_Analysis_PCA
            ii. http://www.vision.jhu.edu/teaching/vision08/Handouts/case_study_pca1.pdf

    :param mtrx: list of lists of floats
    :return: indices
    """

    # Logarithmic-transformation:
    # stand = np.log(mtrx)

    # Zscore:
    # stand = st.zscore(mtrx, axis=0, ddof=1)

    if not isinstance(mtrx, np.ndarray):
        mtrx = np.asarray(mtrx)


        if not isinstance(mtrx[0], np.ndarray):
            for i in range(len(mtrx)):

                if isinstance(mtrx[0][0], float):
                    mtrx[i] = np.asarray(mtrx[i], dtype=np.float_)
                elif isinstance(mtrx[0][0], int):
                    mtrx[i] = np.asarray(mtrx[i], dtype=np.int)
                elif isinstance(mtrx[0][0], long):
                    mtrx[i] = np.asarray(mtrx[i], dtype=np.long)

    stand = (mtrx - np.mean(mtrx))/np.std(mtrx)

    # Covariance Matrix
    data = covariance(stand)

    # Eigenvalues and Eigenvectors
    eigs = nl.eig(data)

    # Keep real parts & magnitude
    EigVls = abs(eigs[0].real)

    # Determining how many components to keep
    scaled = scale(EigVls)
    principals = np.nonzero(scaled<1.0)[0]



    print "Matrix: \n", \
          "\tRows: ", len(mtrx), "\n", \
          "\tCols: ", len(mtrx[0])
    print "Standardization: \n", \
          "\tRows: ", len(stand), "\n", \
          "\tCols: ", len(stand[0])
    print "EigVals: ", EigVls
    print "Principals: ", principals

    return principals



def detect(pair_map, d, motifName):
    """

    :param matrices:
    :param comparisons:
    :param d: * ADJUST * -> account for d
    :return:
    """

    matches = []
    # # print motifName
    # if motifName == "A_135l_3_2_1_17":
    #     print "Comparisons: \n", \
    #         "Num Rows", len(pair_map['comparisons']), \
    #         "\nNum Cols", len(pair_map['comparisons'][0]), \
    #         "\nRows", rows, \
    #         "\nColumns", cols

    comp = pair_map["comparisons"]
    dist = pair_map["distances"]

    sizes = []
    for matrix in comp:
        for row in matrix:
            if sizes == []:
                sizes.append(len(row))
            else:
                if len(row) not in sizes:
                    sizes.append(len(row))
        if len(sizes) > 1:
            print motifName
            QUIT = raw_input("Do you want to stop?")
            if QUIT == "y":
                quit()
            else:
                continue

    sizes = []
    for matrix in dist:
        for row in matrix:
            if sizes == []:
                sizes.append(len(row))
            else:
                if len(row) not in sizes:
                    sizes.append(len(row))
        if len(sizes) > 1:
            print motifName
            QUIT = raw_input("Do you want to stop?")
            if QUIT == "y":
                quit()
            else:
                continue




    print "Comparisons: \n", \
          "=====================\n" \
          "\tRows: ", len(pair_map['comparisons']), "\n", \
          "\tCols: ", len(pair_map['comparisons'][0]), "\n", \
           "Distances:\n" \
          "=====================\n" \
          "\tRow 1: ", pair_map['distances'][0], "\n"


    if len(pair_map['comparisons']) > 10 and len(pair_map['comparisons'][0]) > 10:
        finalData = usePCA(pair_map, "B")
    elif len(pair_map['comparisons']) <= 10:
        finalData = usePCA(pair_map, "R")
    elif len(pair_map['comparisons'][0]) <= 10:
        finalData = usePCA(pair_map, "C")
    else:
        finalData = pair_map['comparisons']



    searches = []
    cl = 0
    for clus in finalData:
    # for clus in pair_map['comparisons']:

        # Initialize for each cluster
        atom2 = []
        r = []

        # Recall:
        #   comparison tuple looks like:
        #       (atom1, res1, atom2, res2, r)


        for at in clus:
            atom2.append(str(at[2]))
            r.append(d*float(at[4]))
        atom1 = str(clus[0][0])
        res1 = str(clus[0][1])
        res2 = str(clus[0][3])
        searches.append(Cluster(atom1, atom2, res1, res2, r, cl))
        cl+=1

    i = 0
    time = {}
    for cluster in searches:
        i += 1
        # print cluster.__str__()
        results = matchEach(r=cluster.dist, res1=cluster.res1, atom1=cluster.atom1, res2 = cluster.res2, atom2 = cluster.atom2, motifName=motifName, i=i)
        if results != None:
            match, totTime = results
            key = "cluster" + str(i)
            time[key] = totTime
            matches.append(match)
        else:
            return []

    return matches, time




def usePCA(pair_map, pca):

    if pca == "B":

        cols = pca(pair_map['distances'])
        rows = pca(np.transpose(pair_map['distances']))

        pair_map['comparisons'] = np.asarray(pair_map['comparisons'])
        pair_map['comparisons'] = pair_map['comparisons'][cols]

        transpose = []
        k = 0

        map = {}
        # new rows
        for nR in rows:
            map[nR] = []

        for row in pair_map['comparisons']:
            for j in rows:
                map[j].append(row[j])
        for row in map:
            transpose.append(np.asarray(map[row]))

        map = {}
        # new rows
        for nR in range(len(cols)):
            map[nR] = []

        finalData = []
        for row in transpose:
            for j in range(len(row)):
                map[j].append(row[j])
        for row in map:
            finalData.append(np.asarray(map[row]))

    elif pca == "R":

        transpose = []
        map = {}

        for nR in range(len(pair_map['comparisons'])):
            map[nR] = []

        rows = pca(np.transpose(pair_map['distances']))
        for row in pair_map['comparisons']:
            for j in rows:
                map[j].append(row[j])
        for row in map:
            transpose.append(np.asarray(map[row]))

        finalData = []
        for row in transpose:
            for j in range(len(row)):
                map[j].append(row[j])
        for row in map:
            finalData.append(np.asarray(map[row]))

    elif pca == "C":
        cols = pca(pair_map['distances'])
        pair_map['comparisons'] = np.asarray(pair_map['comparisons'])
        pair_map['comparisons'] = pair_map['comparisons'][cols]
        finalData = pair_map['comparisons']

    else:
        raise Exception("usePCA failed: Need to specify what you want to implement PCA onto:\n"
                        "OPTIONS:\n"
                        "\tC: columns\n"
                        "\tR: rows\n"
                        "\tB: both rows and columns")
    return finalData
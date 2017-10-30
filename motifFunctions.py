import config
import time as t
import numpy as np
import numpy.linalg as nl
import pandas as pd
import scipy.stats as st
import os
import mysql.connector
import pandas as pd

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



def select(matrices, comparisons, selection, resPairs):
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

    for pie in sele:
        if pie == 'n.':
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
                    resComp = buildKey(res1, res2, resPairs)
            else:
                if pie != 'w.' and pie != 'of':
                    res2 = pie.upper()
                    resComp = buildKey(res1, res2, resPairs)
    try:
        if resComp == () or atom1 == "" or atom2 == "" or res1 == "" or res2 == "":
            raise Warning
    except:
        raise Warning
    # Build list of matches
    buildDicts(resComp, comparisons, matrices, atom1, res1, atom2, res2, r)


def modifyName(res, pair):
    "How many I's? in residue"
    eye = ""
    flag = False

    ra = pair[0][:len(pair[0]) - 1]
    rb = pair[1][:len(pair[1]) - 1]

    for i in range(len(res) - 1, -1, -1):

        if ra + eye == res:
            return ra + eye + pair[0][len(pair[0]) - 1], 0
        elif rb + eye == res:
            return rb + eye + pair[1][len(pair[1]) - 1], 1

        elif res[i] == "I" and flag == False:
            eye += res[i]

        elif res[i] != "I":
            break

    r1 = pair[0][:len(pair[0]) - 1] + eye
    r2 = pair[1][:len(pair[1]) - 1] + eye

    return r1, r2

def buildKey(res1,res2,resPairs):
    """
    Builds key for matrix dictionaries -> accounts for duplicate residues in
    :param res1: res name 1
    :param res2: res name 2
    :param resPairs: list of possible residues for motif file
    :return: tuple containing names of residue 1 and 2 with index
    """
    # print "Res 1: ", res1
    # print "Res 2: ", res2

    # Test cases:
    if res1[-1] != "I" and len(res1) > 3:
        print "What is res1? ", res1
    if res2[-1] != "I" and len(res1) > 3:
        print "What is res2?", res2

    d = {}

    res1_op1 = []
    res1_op2 = []

    res2_op1 = []
    res2_op2 = []


    for pair in resPairs:

        data1 = modifyName(res1, pair)
        data2 = modifyName(res2, pair)

        if isinstance(data1[1], str) and isinstance(data2[1], str):
            r11, r21 = data1
            r12, r22 = data2

            if res1 == r11 and res2 == r22:
                p1 = r11 + pair[0][len(pair[0]) - 1]
                p2 = r22 + pair[1][len(pair[1]) - 1]
                return (p1, p2)
            elif res1 == r21 and res2 == r12:
                p1 = r21 + pair[1][len(pair[1]) - 1]
                p2 = r12 + pair[0][len(pair[0]) - 1]
                return (p1, p2)

        elif isinstance(data1[1], str):
            r11, r21 = data1
            r2 = data2[0]

            if data2[1] == 0:
                if res1 == r21 and res2 == r2:
                    r1 = r21 + pair[1][len(pair[1]) - 1]
                    return (r1, r2)

            elif data2[1] == 1:
                if res1 == r11 and res2 == r2:
                    r1 = r11 + pair[0][len(pair[0]) - 1]
                    return (r1, r2)

        elif isinstance(data2[1], str):
            r1 = data1[0]
            r12, r22 = data2

            if data1[1] == 0:
                if res1 == r1 and res2 == r22:
                    r2 = r22 + pair[1][len(pair[1]) - 1]
                    return (r1, r2)

            elif data2[1] == 1:
                if res1 == r1 and res2 == r12:
                    r2 = r12 + pair[0][len(pair[0]) - 1]
                    return (r1, r2)
        else:
            return (data1[0], data2[0])


    d["[R1_O1]"] = res1_op1
    d["[R1_O2]"] = res1_op2
    d["[R2_O1]"] = res2_op1
    d["[R2_O2]"] = res2_op2
    table(d, res1, res2, resPairs)

def table(d, res1, res2, lst):
    tbl = pd.DataFrame(d)
    print "Residues: ", (res1, res2)
    print "From Motif: ", lst
    print tbl
    quit()


def buildDicts(resComp, comparisons, matrices, atom1, res1, atom2, res2, r, FLAG=False):
    """
    builds current line from current motif onto comparisons dictionary (comparisons)
    and distance dictionary (matrices)

    post-condition : each element in each value in comparisons (dictionary) consists of a tuple in this exact order:
        element = (atom1, res1, atom2, res2, r)

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
    if resComp not in matrices:
        for pairs in comparisons:

            # print "Res Comp: ", resComp
            # print "Pairs: ", pairs
            # print "Res1: ", res1, "res2: ", res2

            if resComp[0] == pairs[1] and resComp[1] == pairs[0]:
                return
        matrices[resComp] = [r]
        comparisons[resComp] = [(atom1, res1, atom2, res2, r)]
        FLAG = True


    elif type(comparisons[resComp][-1]) == list:
        if comparisons[resComp][-1][-1][1] != res1 or comparisons[resComp][-1][-1][3] != res2:
            # Make new matrix
            # print "Res1 in cluster: ", comparisons[resComp][-1][-1][1]
            # print "Res2 in cluster: ", comparisons[resComp][-1][-1][3]
            #
            # print "Res1: ", res1
            # print "Res2: ", res2
            raise Warning
        elif comparisons[resComp][-1][-1][0] == atom1:
            comparisons[resComp][-1].append((atom1, res1, atom2, res2, r))
            matrices[resComp][-1].append(r)
        else:
            comparisons[resComp].append([(atom1, res1, atom2, res2, r)])
            matrices[resComp].append([r])

    elif type(comparisons[resComp][-1]) == tuple:
        if comparisons[resComp][-1][0] == atom1:
            comparisons[resComp].append((atom1, res1, atom2, res2, r))
            matrices[resComp].append(r)
        else:
            comparisons[resComp] = [comparisons[resComp], [(atom1, res1, atom2, res2, r)]]
            matrices[resComp] = [matrices[resComp], [r]]

    else:
            print("Error: Dictionary should contain Match objects / Lists of Match objects / List of lists of Match objects")

    return comparisons, matrices, resComp, FLAG



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
                    print " I went here!"
                    mtrx[i] = np.asarray(mtrx[i], dtype=np.long)

    #
    # else:
    #     mtrx = m

    # m = []
    # if not isinstance(mtrx[0], np.ndarray):
    #     for row in mtrx:
    #         row = np.asarray(row)
    #         m.append(row)
    #     m = np.asarray(m)
    #
    #     mtrx = m


    stand = (mtrx - np.mean(mtrx))/np.std(mtrx)

    # Covariance Matrix
    data = covariance(stand)

    # Eigenvalues and Eigenvectors
    eigs = nl.eig(data)

    # Keep real parts & magnitude
    EigVls = abs(eigs[0].real)

    # Determining how many components to keep
    principals = []

    scaled = scale(EigVls)
    # I = set()
    # J = set()
    # for i in range(len(scaled)-1):
    #     if scaled[i] != 0.0:
    #         for j in range(len(scaled)-1):
    #             if scaled[j] != 0.0:
    #                 if i != j:
    #                     I.add(i)
    #                     J.add(j)
    # if I == J:
    #     principals = list(I)
    # elif len(I) > len(J) or len(I) < len(J):
    #     for i in I:
    #         for j in J:
    #             if i == j:
    #                 principals.append(i)
    # else:
    #     print "Error: Algorithm failed."

    principals = np.nonzero(scaled>0.0)[0]




    # ave = average(scaled)
    # principals = np.nonzero(EigVls >= ave)[0]

    # k = 1
    # while len(rest) > len(principals) and k < 5:
    #
    #     # Find average eigenvalue w/o outliers:
    #     scaled = []
    #     others = EigVls[rest]
    #     print others
    #
    #     min = np.min(others)
    #     max = np.max(others)
    #
    #     for eig in others:
    #         scaled.append((eig - min) / (max - min))
    #     scaled = np.asarray(scaled)
    #     ave = average(scaled)
    #     principals = np.nonzero(EigVls >= ave)[0]
    #
    #     rest = []
    #     for e in range(len(EigVls)):
    #         if e <= len(principals)-1:
    #             if e != principals[e]:
    #                 rest.append(e)
    #         else:
    #             rest.append(e)
    #     k+=1

    # while len(principals) < len(EigVls)/2:
    #     # Decide to: Compare to an int (*) or float
    #     # Find a way to just remove the super tiny eigenvalues and not the kinda small eigenvalues
    #     principals = np.nonzero(EigVls >= var)[0]
    #     var /= 10.
    return principals



def detect(pair_map, d, motifName):
    """

    :param matrices:
    :param comparisons:
    :param d: * ADJUST * -> account for d
    :return:
    """



    matches = []
    np.set_printoptions(suppress=True)

    cols = pca(pair_map['distances'])
    rows = pca(np.transpose(pair_map['distances']))

    before = np.asarray(pair_map['comparisons'])
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

    searches = []
    cl = 0
    for clus in finalData:

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
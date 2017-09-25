import config
import time as t
import numpy as np
import numpy.linalg as nl
import scipy.stats as st

class Cluster(object):
    def __init__(self, atom1, atom2, res1, res2, r):
        self.atom1 = atom1
        self.atom2 = atom2
        self.res1 = res1
        self.res2 = res2
        self.dist = r


def match(name, matches, r, res1, atom1, res2, atoms):
    before = t.time()
    matches[name] = config.TREE.query_pairs(r=r, res1=res1, atomName1=atom1, res2=res2, atomName2=atoms)
    # print("Match: ", name, t.time() - before)
    if matches[name] == list():
        matches = {}
        print "Motif failed!"
        quit()

def matchEach(r, res1, atom1, res2, atom2):
    match = config.TREE.query_pairs(r=r, res1=res1, atomName1=atom1, res2=res2, atomName2=atom2)
    if match == dict():
        print "Motif failed!"
    return match

def select(matrices, comparisons, selection):
    """

    :param matrices: distance matrix
    :param comparisons: matrix of comparison objects
    :param selection: selection algebra
    :return: updated matrices
    """
    flag = False
    if selection == "n. CB&r. his w. 7.57 of n. CB&asp":
        flag = True
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
                    resComp = (res1, res2)
            else:
                 if pie != 'w.' and pie != 'of':
                        res2 = pie.upper()
                        resComp = (res1, res2)
    try:
        if resComp == () or atom1 == "" or atom2 == "" or res1 == "" or res2 == "":
            raise Warning
    except:
        raise Warning
    # Build list of matches
    buildDicts(resComp, comparisons, matrices, atom1, res1, atom2, res2, r)


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
    :return: 
    """
    if resComp not in matrices:
        for pairs in comparisons:
            if resComp[0] == pairs[1] and resComp[1] == pairs[0]:
                return
        matrices[resComp] = [r]
        comparisons[resComp] = [(atom1, res1, atom2, res2, r)]
        FLAG = True

    elif type(comparisons[resComp][-1]) == list:
        if comparisons[resComp][-1][-1][1] != res1 or comparisons[resComp][-1][-1][3] != res2:
            # Make new matrix
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
        mrtx = np.asarray(mtrx)
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
    print principals
    return principals



def detect(pair_map, d):
    """

    :param matrices:
    :param comparisons:
    :param d: * ADJUST * -> account for d
    :return:
    """
    matches = []
    np.set_printoptions(suppress=True)

    rows = pca(pair_map['distance'])
    cols = pca(np.transpose(pair_map['distance']))

    pair_map['comparisons'] = np.asarray(pair_map['comparisons'])
    pair_map['comparisons'] = pair_map['comparisons'][rows]

    T = np.transpose(pair_map['comparisons'])
    pair_map['comparisons'] = np.transpose(T[cols])

    searches = []
    for clus in pair_map['comparisons']:

        # Initialize for each cluster
        atom2 = []
        r = []

        # Recall:
        #   comparison tuple looks like:
        #       (atom1, res1, atom2, res2, r)

        for at in clus:
            atom2.append(at[2])
            r.append(at[4])
        atom1 = clus[0][0]
        res1 = clus[0][1]
        res2 = clus[0][3]
        searches.append(Cluster(atom1, atom2, res1, res2, r))

    for cluster in searches:
        matches.append(matchEach(r=cluster.dist, res1=cluster.res1, atom1=cluster.atom1, res2 = cluster.res2, atom2 = cluster.atom2))
    return matches
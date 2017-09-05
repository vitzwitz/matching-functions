import config
import time as t
import numpy as np
import numpy.linalg as nl
import scipy.stats as st

class Comparison(object):
    def __init__(self, atom1, atom2, res1, res2):
        self.atom1 = atom1
        self.atom2 = atom2
        self.res1 = res1
        self.res2 = res2


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

def select(matches, comparisons, selection):
    """

    :param matches: list of matches
    :param comparisons: distance matrix
    :param selection: selection algebra
    :return:
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
            if pie[-3:] == '&r.':
                atom2 = pie.strip('&r.')
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
    buildDicts(resComp, matches, comparisons, atom1, res1, atom2, res2, r)




def buildDicts(resComp, matches, comparisons, atom1, res1, atom2, res2, r):
    """
    builds current line from current motif onto comparisons dictionary (comparisons)
    and distance dictionary (comparisons)

    :param resComp: pair of residue names
    :param matches: dictionary of matrices of atoms to compare
    :param comparisons: dictionary of distance matrices 
    :param atom1: atom name for current row that's being built 
    :param res1: residue name for current matrix that's being built
    :param atom2: atom name for element that's being built in matches 
    :param res2: residue name for current matrix that's being built in matches
    :param r: distance for current element that's being built in comparisons
    :return: 
    """

    if resComp in matches and resComp in comparisons:
        if type(matches[resComp][-1]) == list:
            if matches[resComp][-1][-1].res1 != res1 or matches[resComp][-1][-1].res2 != res2:
                # Make new matrix
                raise Warning
            elif matches[resComp][-1][-1].atom1 == atom1:
                matches[resComp][-1].append(Comparison(atom1, atom2, res1, res2))
                comparisons[resComp][-1].append(r)
            else:
                matches[resComp].append([Comparison(atom1, atom2, res1, res2)])
                comparisons[resComp].append([r])
        elif type(matches[resComp][-1]) == Comparison:
            if matches[resComp][-1].atom1 == atom1:
                matches[resComp].append(Comparison(atom1, atom2, res1, res2))
                comparisons[resComp].append(r)
            else:
                matches[resComp] = [matches[resComp], [Comparison(atom1, atom2, res1, res2)]]
                comparisons[resComp] = [comparisons[resComp], [r]]

        else:
            print("Error: Dictionary should contain Match objects / Lists of Match objects / List of lists of Match objects")

    if resComp not in comparisons:
        comparisons[resComp] = [r]
    if resComp not in matches:
        matches[resComp] = [Comparison(atom1, atom2, res1, res2)]



def covariance(mtrx):
    """
    Build covariance matrix from given matrix

    Citation : http://www.cs.toronto.edu/~guerzhoy/320/lec/pca.pdf
    :param mtrx: matrix
    :return: covariance matrix of given matrix
    """

    # Average column of matrix
    ave = np.zeros(len(mtrx[0]))
    i = 0
    for row in mtrx:
        if type(mtrx) == list:
            ave += np.asarray(row)
            mtrx[i] = np.asarray(row)
            i+=1
        elif type(mtrx) == np.ndarray:
            ave += row
    ave /= len(mtrx[0])

    # Covariance matrix
    return np.dot((mtrx - ave), np.transpose(mtrx - ave))



def pca(mtrx):
    dof = len(mtrx) - len(mtrx[0])

    # Standardize distance matrix
    if dof < 0:
        stand = st.zscore(mtrx, axis=0, ddof=abs(dof))
        np.append(mtrx, np.zeros([abs(dof), len(mtrx[0])]))
    elif dof > 0:
        stand = st.zscore(mtrx, axis=1, ddof=abs(dof))
        for row in mtrx:

    else:
        stand = st.zscore(mtrx)

    # Eigenvalues and Eigenvectors

    # eigs = nl.eig(covariance(stand))

    eigs = nl.eig(mtrx)
    print "***************"

    # Determining how many components to keep
    principles = np.zeros(0)
    var = 0.95
    while len(principles) < len(eigs[0])/2.:
        principles = np.nonzero(eigs[0] >= var)[0]
        var /= 10.
    # print "Number of eigenvalues: ", len(eigs[0])
    # print "Eigenvalues: \n", eigs[0]
    print principles, '\n'

    return principles



def detect(comparisons):
    pass

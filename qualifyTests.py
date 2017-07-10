import numpy as np
import Classes as cl
from ParseOnlyAtoms import *


def qualifyingHelper(a, dist, distance_upper_bound, orEqual, atomName, res):
    qualified = []
    if len(a) == 1:
        return isQualified(a, dist, distance_upper_bound, orEqual, atomName, res)
    if isinstance(a[0], cl.Atom):
        for at in range(len(a)):
            qualified.append(isQualified(a[at], dist[at], distance_upper_bound, orEqual, atomName, res))
    else:
        raise Warning
    return np.asarray(qualified)

def isQualified(a, dist, distance_upper_bound, orEqual="", atomName="", res=""):
    if not isinstance(a, cl.Atom):
        if len(a) > 1:
            return qualifyingHelper(a, dist, distance_upper_bound, orEqual, atomName, res)
        elif len(a) == 1:
            a = a[0]
            dist = dist[0]
            return isQualified(a, dist, distance_upper_bound, orEqual="", atomName="", res="")
        else:
            raise Warning
    else:
        if (dist >= distance_upper_bound and orEqual=="") or (dist > distance_upper_bound and orEqual=="="):
            return False
        if atomName != "" and a.name != atomName:
            return False
        if res != "" and a.resName != res:
            return False
        return True

def TestThis():
    pdbID = raw_input("Enter a pdb code: ")
    path = urllib.urlretrieve('http://files.rcsb.org/download/%s.pdb' % pdbID,
                              'C:/Users/Brianna/PycharmProjects/ClusterAlg/%s.pdb' % pdbID)
    try:
        file = 'C:/Users/blm7643/Downloads/proteinDATA/%s.pdb' % pdbID
        pdbData = readFile(file)
    except IOError:
        file = '%s.pdb' % pdbID
        pdbData = readFile(file)
    Atoms = pdbData["Atom"]
    # print "Testing Atom", Atoms[0].name, Atoms[0].resName
    # print("Test 1: QUALIFIED -> 1 atom ; dist", isQualified(Atoms[0], 1.52, 2.13, orEqual="", atomName="", res=""))
    # print("Test 2: UNQUALIFIED -> 1 atom ; dist", isQualified(Atoms[0], 2.31, 1.52, orEqual="", atomName="", res=""))

    # print("Test 3: QUALIFIED -> 1 atom ; dist, name", isQualified(Atoms[0], 1.52, 2.13, "", "N", res=""))
    # print("Test 4: UNQUALIFIED -> 1 atom ; dist, name", isQualified(Atoms[0], 1.2, 1.52, "", "CB", res=""))

    # print("Test 5: QUALIFIED -> 1 atom ; dist, res", isQualified(Atoms[0], 1.52, 2.13, "", "", "ALA"))
    # print("Test 6: UNQUALIFIED -> 1 atom ; dist, res", isQualified(Atoms[0], 11.2, 1.52, "", "", "GLU"))

    # print("Test 7: QUALIFIED -> 1 atom ; dist, name, res", isQualified(Atoms[0], 1.52, 2.13, "", "N", "ALA"))
    # print("Test 8: UNQUALIFIED -> 1 atom ; dist, name, res", isQualified(Atoms[0], 1.2, 1.52, "", "CB", "GLU"))

    # print("Test 9: QUALIFIED -> 1 atom ; dist, <=", isQualified(Atoms[0], 1.52, 4.52, "=", "", res=""))
    # print("Test 10: QUALIFIED -> 1 atom ; dist, =", isQualified(Atoms[0], 1.52, 1.52, "=", "", res=""))
    # print("Test 11: UNQUALIFIED -> 1 atom ; dist, >", isQualified(Atoms[0], 1.52, 1.0, "=", "", res=""))

    # print("Test 12: QUALIFIED -> 1 atom ; dist, name, =", isQualified(Atoms[0], 1.52, 2.13, "=", "N", ""))
    # print("Test 13: UNQUALIFIED -> 1 atom ; dist, name =", isQualified(Atoms[0], 1.2, 1.25, "=", "CB", ""))

    # print("Test 14: QUALIFIED -> 1 atom ; dist, name, res =", isQualified(Atoms[0], 1.52, 2.13, "=", "N", "ALA"))
    # print("Test 15: UNQUALIFIED -> 1 atom ; dist, name, res =", isQualified(Atoms[0], 1.2, 1.52, "=", "CB", "GLU"))

    print Atoms[1].name, Atoms[1].resName, Atoms[2].name, Atoms[2].resName
    # print("Test 16: QUALIFIED -> mult atoms ; dist", isQualified(Atoms[1:3], [1.52, 2.01], 2.13))
    # print("Test 17: UNQUALIFIED -> mult atoms ; dist", isQualified(Atoms[1:3], [1.52, 2.01], 0.13))

    # print("Test 18: QUALIFIED -> mult atoms ; dist, name", isQualified(Atoms[1:3], [1.52, 2.01], 2.13, atomName="CA"))
    # print("Test 19: UNQUALIFIED -> mult atoms ; dist, name", isQualified(Atoms[1:3], [1.52, 2.01], 2.13, atomName="O"))

    # print("Test 20: QUALIFIED -> mult atoms ; dist, res", isQualified(Atoms[1:3], [1.52, 2.01], 2.13, res="ALA"))
    # print("Test 21: UNQUALIFIED -> mult atoms ; dist, res", isQualified(Atoms[1:3], [1.52, 2.01], 2.13, res="GLU"))

    # print("Test 22: QUALIFIED -> mult atoms ; dist, =", isQualified(Atoms[1:3], [2.13, 2.13], 2.13, orEqual="="))
    # print("Test 23: UNQUALIFIED -> mult atoms ; dist, =", isQualified(Atoms[1:3], [2.5, 2.9], 2.13, orEqual="="))

    print("Test 24: QUALIFIED -> mult atoms ; dist, name, res", isQualified(Atoms[1:3], [1.52, 2.01], 2.13, atomName="CA", res="ALA"))
    print("Test 25: UNQUALIFIED -> mult atoms ; dist, name, res", isQualified(Atoms[1:3], [1.52, 2.01], 2.13, atomName="CA", res="GLU"))

TestThis()
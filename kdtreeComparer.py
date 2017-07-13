import numpy as np
import scipy
from scipy import spatial

import Classes as cl
from ParseOnlyAtoms import *

def getAtoms():
    # pdbID = raw_input("Enter a pdb code: ")
    pdbID = "1a0j"
    path = urllib.urlretrieve('http://files.rcsb.org/download/%s.pdb' % pdbID,
                              'C:/Users/Brianna/PycharmProjects/ClusterAlg/%s.pdb' % pdbID)
    try:
        file = 'C:/Users/blm7643/Downloads/proteinDATA/%s.pdb' % pdbID
        pdbData = readFile(file)
    except IOError:
        file = '%s.pdb' % pdbID
        pdbData = readFile(file)
    return pdbData["Atom"]

def Comparer():
    pts = []
    ATOMS = getAtoms()
    for pos in ATOMS:
        pts.append(pos.position)
    TREE = spatial.KDTree(pts)
    pairs = TREE.query_pairs(10.70)
    print(len(list(pairs)))
    # neighS = treee.query_pairs(r=10.70, res1="CYS", res2="GLU", atomName1="CB", atomName2="OE2")
    if np.all(TREE.data == pts):
        print "Not re-sorted"
    else:
        print("Re-sorted")

    for ackr in list(pairs):
        if (ATOMS[ackr[1]].name == "OE2" and ATOMS[ackr[1]].resName == "GLU") and (ATOMS[ackr[0]].name == "CB" and ATOMS[ackr[0]].resName == "CYS"):
            print("CB CYS", "OE2 GLU")
        if (ATOMS[ackr[0]].name == "OE2" and ATOMS[ackr[0]].resName == "GLU") and (ATOMS[ackr[1]].name == "CB" and ATOMS[ackr[1]].resName == "CYS"):
            print("OE2 GLU", "CB CYS")

Comparer()
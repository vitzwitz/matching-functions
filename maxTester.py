import numpy as np
import Classes as cl
from ParseOnlyAtoms import *
# import kdtrees4atoms as kdt

def indexHelper(i, atom):

    if i==0: return atom.x
    elif i==1: return atom.y
    elif i==2: return atom.z
    else: raise Warning

def minmaxBC(atoms, d=""):
    if d == "":
        d = [0,1,2]
    if isinstance(d,int):
        if d==0:
            maxes = atoms[0].x
            mins = atoms[0].x
        elif d==1:
            maxes = atoms[0].y
            mins = atoms[0].y
        elif d==2:
            maxes = atoms[0].z
            mins = atoms[0].z
    elif isinstance(d,list) or isinstance(d,tuple):
        mins = list(atoms[0].position)
        maxes = list(mins)
    else:
        raise Warning
    for atom in atoms:
        if isinstance(d, int):
            if indexHelper(d,atom) < mins:
                mins = indexHelper(d,atom)
            if indexHelper(d,atom) > maxes:
                maxes = indexHelper(d,atom)
        elif isinstance(d, list) or isinstance(d, tuple):
            for j in d:
                if indexHelper(j,atom) < mins[j]:
                    mins[j] = indexHelper(j,atom)
                if indexHelper(j,atom) > maxes[j]:
                    maxes[j] = indexHelper(j,atom)
    return np.asarray(mins), np.asarray(maxes)

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

def testIndexHelper():
    # TREE = kdt.KDTree4Atoms(getAtoms())
    atom = getAtoms()[0]
    print atom.position
    print "Test 1", indexHelper(0, atom)
    print "Test 2", indexHelper(1, atom)
    print "Test 3", indexHelper(2, atom)

def testMinMax():
    atom = getAtoms()
    mins, maxes = minmaxBC(atom, d="")
    print "mins:", list(mins)
    print "maxes:", list(maxes)
    n = np.shape(atom)[0]
    m = np.shape(np.asarray(atom[0].position))[0]
    print "m=3", m, "n=6640", n
testMinMax()
import kdtree4atoms as kdt
import numpy as np
import ParserOnlyAtoms as poa
import os

# 2o2z,

# Small family
TREEs = {}
familyData = {}
for pdb in open('babyFamily.txt'):
    pdb = pdb.strip("\n")
    # Retrieve files
    path = poa.urllib.urlretrieve('http://files.rcsb.org/download/%s.pdb' % pdb,
                                  'C:/Users/Brianna/PycharmProjects/optimizer/%s.pdb' % pdb)
    try:
        file = 'C:/Users/blm7643/Downloads/kdtree/%s.pdb' % pdb
        pdbData = poa.readFile(file)
    except IOError:
        file = '%s.pdb' % pdb
        pdbData = poa.readFile(file)

    Atoms = pdbData["Atom"]
    TREEs[pdb] = kdt.KDTree4Atoms(np.asarray(Atoms))
    familyData[pdb] = ""

# Big family

TREEs = {}
familyData = {}
for pdb in open('serineProtease.txt'):
    pdb = pdb.strip("\n")
    # Retrieve files
    path = 'pdbFiles'
    if not os.path.exists(path):
        os.makedirs(path)

    PATH = poa.urllib.urlretrieve('http://files.rcsb.org/download/%s.pdb' % pdb,
                                  'C:/Users/Brianna/PycharmProjects/optimizer/%s/%s.pdb' % (path, pdb))
    try:
        file = 'C:/Users/blm7643/Downloads/optimizer/%s/%s.pdb' % (path, pdb)
        pdbData = poa.readFile(file)
    except IOError:
        file = '%s/%s.pdb' % (path, pdb)
        pdbData = poa.readFile(file)

    Atoms = pdbData["Atom"]
    TREEs[pdb] = kdt.KDTree4Atoms(np.asarray(Atoms))
    familyData[pdb] = ""
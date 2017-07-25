import kdtrees4atoms as kdt
import numpy as np
import ParseOnlyAtoms as poa
import time as t

pdbID = '1a0j'
path = poa.urllib.urlretrieve('http://files.rcsb.org/download/%s.pdb' % pdbID,
                          'C:/Users/Brianna/PycharmProjects/ClusterAlg/%s.pdb' % pdbID)
try:
    file = 'C:/Users/blm7643/Downloads/proteinDATA/%s.pdb' % pdbID
    pdbData = poa.readFile(file)
except IOError:
    file = '%s.pdb' % pdbID
    pdbData = poa.readFile(file)

Atoms = pdbData["Atom"]
TREE = kdt.KDTree4Atoms(np.asarray(Atoms))
import kdtree4atoms as kdt
import numpy as np
import ParserOnlyAtoms as poa

pdbID = '1a0j'
path = poa.urllib.urlretrieve('http://files.rcsb.org/download/%s.pdb' % pdbID,
                          'C:/Users/Brianna/PycharmProjects/optimizer/%s.pdb' % pdbID)
try:
    file = 'C:/Users/blm7643/Downloads/kdtree/%s.pdb' % pdbID
    pdbData = poa.readFile(file)
except IOError:
    file = '%s.pdb' % pdbID
    pdbData = poa.readFile(file)

Atoms = pdbData["Atom"]
TREE = kdt.KDTree4Atoms(np.asarray(Atoms))
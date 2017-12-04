import kdtree4atoms as kdt
import numpy as np
import ParserOnlyAtoms as poa
import os



#***# Already made
# motifData = {}
# for line in open("C:/Users/Brianna/PyCharmProjects/optimizer/Data/motifNames.txt"):
#     name = line.strip("\n")
#     motifData[name] += 'Motif : ' + name + "\n"

# Extra :
#     motifData[name] = '"""\n'
#     motifData[name] += "Data File Containing Results from Search Algorithm for Serine Protease for:"
#     motifData[name] += "Author: Bri Miskovitz"
#     motifData[name] += '"""'

# Very Small family
TREEs = {}
# for pdb in open('/home/michael/Documents/Git/bris_research/research/matching-functions-master/immediateFamily.txt'):
#     pdb = pdb.strip("\n")
#     print pdb
#     # Retrieve files
#     path = '/home/michael/Documents/Git/bris_research/research/matching-functions-master/pdbFiles'
#     if not os.path.exists(path):
#         os.makedirs(path)
#
#
#     PATH = poa.urllib.urlretrieve('http://files.rcsb.org/download/%s.pdb' % pdb,
#                                   '%s/%s.pdb' % (path, pdb))
#
#     # print "Path:", PATH
#     try:
#         file = '\\home\\michael\\Documents\\Git\\bris_research\\research\\matching-functions-master\\pdbFiles\\%s\\%s.pdb' % (path, pdb)
#         pdbData = poa.readFile(file)
#     except IOError:
#         pth = '\\home\\michael\\Documents\\Git\\bris_research\\research\\matching-functions-master\\pdbFiles'
#         file = '%s\\%s.pdb' % (pth, pdb)
#         print "FILE:", file

pdb = '1a0j'
file = '/home/michael/Documents/Git/bris_research/research/matching-functions/pdbFiles/1a0j.pdb'
pdbData = poa.readFile(file)


Atoms = pdbData["Atom"]
TREEs[pdb] = kdt.KDTree4Atoms(np.asarray(Atoms))


# Big family

# TREEs = {}
# familyData = {}
# for pdb in open('serineProtease.txt'):
#     pdb = pdb.strip("\n")
#     # Retrieve files
#     path = 'pdbFiles'
#     if not os.path.exists(path):
#         os.makedirs(path)
#
#     PATH = poa.urllib.urlretrieve('http://files.rcsb.org/download/%s.pdb' % pdb,
#                                   'C:/Users/Brianna/PycharmProjects/optimizer/%s/%s.pdb' % (path, pdb))
#     try:
#         file = 'C:/Users/blm7643/Downloads/optimizer/%s/%s.pdb' % (path, pdb)
#         pdbData = poa.readFile(file)
#     except IOError:
#         file = '%s/%s.pdb' % (path, pdb)
#         pdbData = poa.readFile(file)
#
#     Atoms = pdbData["Atom"]
#     TREEs[pdb] = kdt.KDTree4Atoms(np.asarray(Atoms))
#     familyData[pdb] = ""
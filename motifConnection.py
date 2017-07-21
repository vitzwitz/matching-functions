# import os

from functions import *
from ParseOnlyAtoms import *
from Classes import *
# import kdtreeCOPY as kdc
import kdtrees4atoms as kdt
import time as t

def indivSelect(name, selection):
    sel = selection.split()

    if len(sel) == 8:
        atmres = sel[7].split('&')
        pairs = treee.query_pairs(float(sel[4]), sel[2].upper(), sel[1].strip('&r.'), atmres[1], atmres[0])
    if len(sel) == 9:
        pairs = treee.query_pairs(float(sel[4]), sel[2].upper(), sel[1].strip('&r.'), sel[8].upper(), sel[7].strip('&r.'))
    else:
        print(len(sel))
        pairs = set()
    if pairs == set():
        quit()

def select(motifDict, name, selection):

    sel = selection.split()
    if len(sel) == 8:
        atmres = sel[7].split('&')
        motifDict[name] = [float(sel[4]), sel[2].upper(), sel[1].strip('&r.'), atmres[1], atmres[0]]
        # print "I'm here", motifDict[name]
    if len(sel) == 9:
        motifDict[name] = [float(sel[4]), sel[2].upper(), sel[1].strip('&r.'), sel[8].upper(), sel[7].strip('&r.')]
        # print "Naw I'm here", motifDict[name]

def match(motifDict):
    r = []
    atoms = []
    for sln in motifDict:
        r.append(motifDict[sln][0])
        atoms.append(motifDict[sln][-1])
        atm = sln
    res1 = motifDict[atm][1]
    atom1 = motifDict[atm][2]
    res2 = motifDict[atm][-2]

    pairs = treee.query_pairs(r=r, res1=res1, atomName1=atom1, res2=res2, atomName2=atoms)
    if pairs == set():
        quit()


def delete(motifDict):
    del motifDict
    return {}


def simpleTester():
    # pdbID = raw_input("Enter a pdb code: ")
    pdbID = "1a0j"
    path = urllib.urlretrieve('http://files.rcsb.org/download/%s.pdb' % pdbID,
                              'C:/Users/Brianna/PycharmProjects/ClusterAlg/%s.pdb' % pdbID)
    try:
        file = 'C:/Users/blm7643/Downloads/proteinDATA/%s.pdb' % pdbID
        pdbData = readFile(file)
    except IOError:
        # file = '%s.pdb' % pdbID
        pdbData = readFile("1a0j.pdb")
    passedMotifs = {}
    failedMotifs = {}

    File = "2ndCopyofMotif.py"
    Atoms = pdbData["Atom"]

    global d
    global treee

    d = 2
    start = t.time()
    treee = kdt.KDTree4Atoms(np.asarray(Atoms))
    buildTree = t.time() - start
    execfile(File)

def optimizing1():
    pass

simpleTester()
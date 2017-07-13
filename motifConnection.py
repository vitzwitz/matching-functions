# import os

from functions import *
from ParseOnlyAtoms import *
from Classes import *
# import kdtreeCOPY as kdc
import kdtrees4atoms as kdt
import time as t

def select(name, selection):
    sel = selection.split()
    if len(sel) == 8:
        atmres = sel[7].split('&')
        pairs = treee.query_pairs(r=float(sel[4]), atomName1=sel[1].strip('&r.'), res1=sel[2].upper(),
                                  atomName2=atmres[0], res2=atmres[1])
        if pairs == set():
            print "len 8"
            print name
            print "MOTIF FAILED"
            # found on stackoverflow -> https://stackoverflow.com/questions/5788891/execute-a-file-with-arguments-in-python-shell
            quit()
            # update d
    if len(sel) == 9:
        pairs = treee.query_pairs(r=float(sel[4]), atomName1=sel[1].strip('&r.'), res1=sel[2].upper(), atomName2=sel[7].strip('&r.'), res2=sel[8].upper())
        if pairs == set():
            print "len 9"
            print "r=", float(sel[4]), "atomName1=", sel[1].strip('&r.'), "res1=", sel[2].upper(), "atomName2=", sel[7].strip('&r.'), "res2=", sel[8].upper()
            print name
            print "MOTIF FAILED"
            quit()
            # update d



def delete(name):
    # unsure
    print "name:", name

def testMotifConnect(motif):
    File = "A_1a4s_1_2_1_8.py"
    # MOTIFS[func]['path'] = os.path.join(motdir, motifFile)
    motifFile = open(File, 'rU')

    try:
        motifFile.__enter__()
        for line in motifFile:
            pass
    finally:
        motifFile.__exit__()
    d = 1
    execfile(File)

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

    File = "A_1a4s_1_2_1_8.py"
    Atoms = pdbData["Atom"]

    global passedConstraints
    global d
    global treee

    passedConstraints = {}
    d = 2
    start = t.time()
    treee = kdt.KDTree4Atoms(np.asarray(Atoms))
    buildTree = t.time() - start
    execfile(File)
    motif = t.time() - buildTree
    end = t.time() - start

    print "Time to build Tree:", buildTree, "seconds"
    print "Time to go thru motifs:", motif, "seconds"
    print "Time for entire process:", end

def optimizing1():
    pass

simpleTester()
import config
import time as t

def match(name, matches, r, res1, atom1, res2, atoms):
    before = t.time()
    matches[name] = config.TREE.query_pairs(r=r, res1=res1, atomName1=atom1, res2=res2, atomName2=atoms)
    print("Match: ", name, t.time() - before)
    if matches[name] == list():
        matches = {}
        print "Motif failed!"
        quit()

def matchEach(name, matches, r, res1, atom1, res2, atom2):
    matches[name] = config.TREE.query_pairs(r=r, res1=res1, atomName1=atom1, res2=res2, atomName2=atom2)
    print name, '\n', matches[name]
    if matches[name] == list():
        matches = {}
        print "Motif failed!"
        quit()
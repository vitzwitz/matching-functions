import config

def match(r, res1, atom1, res2, atoms):
    pairs = config.TREE.query_pairs(r=r, res1=res1, atomName1=atom1, res2=res2, atomName2=atoms)
    if pairs == set():
        quit()

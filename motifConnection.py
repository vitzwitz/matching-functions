import config
def select(motifDict, name, selection):
    sel = selection.split()
    if len(sel) == 8:
        atmres = sel[7].split('&')
        motifDict[name] = [float(sel[4]), sel[2].upper(), sel[1].strip('&r.'), atmres[1], atmres[0]]
    if len(sel) == 9:
        motifDict[name] = [float(sel[4]), sel[2].upper(), sel[1].strip('&r.'), sel[8].upper(), sel[7].strip('&r.')]

def match(motifDict):
    # print('match:', TreeE)
    r = []
    atoms = []
    for sln in motifDict:
        r.append(motifDict[sln][0])
        atoms.append(motifDict[sln][-1])
        atm = sln
    res1 = motifDict[atm][1]
    atom1 = motifDict[atm][2]
    res2 = motifDict[atm][-2]
    pairs = config.TREE.query_pairs(r=r, res1=res1, atomName1=atom1, res2=res2, atomName2=atoms)
    if pairs == set():
        quit()

def delete(motifDict):
    del motifDict
    return {}


class Match(object):
    def __init__(self, atom1, atom2, res1, res2):
        self.atom1 = atom1
        self.atom2 = atom2
        self.res1 = res1
        self.res2 = res2



def matchList(matches, atom1, atom2, res1, res2):
    try:
        if matches[-2].atom1 == matches[-1][-1].atom1 and matches[-2][-1].res1 == matches[-1][-1].res1 and\
                        matches[-2][-1].res2 == matches[-1][-1].res2:
            matches.append(Match(atom1, atom2, res1, res2))
        else:
            matches.append([Match(atom1, atom2, res1, res2)])
    except:
        if len(matches) == 0:
            matches.append([Match(atom1, atom2, res1, res2)])
        else:
            matches.append(Match(atom1, atom2, res1, res2))


def matrixBuilder(matches, mtrx, resComp, r):
    try:
        if len(mtrx[resComp][0]) > 0:
            if matches[-2].atom1 == matches[-1].atom1 and \
                            matches[-2].res1 == matches[-1].res1 and \
                            matches[-2].res2 == matches[-1].res2:
                mtrx[resComp][-1].append(r)
            else:
                mtrx[resComp].append([r])
    except:
        if len(mtrx[resComp]) > 0:
            print matches
            if matches[-2][-1].atom1 == matches[-1][-1].atom1 and \
                            matches[-2][-1].res1 == matches[-1][-1].res1 and \
                            matches[-2][-1].res2 == matches[-1][-1].res2:
                mtrx[resComp].append(r)
            else:
                mtrx[resComp].append([r])


def testMatrixBuilder():

    glu = ['CB', 'CG', 'CD', 'OE1', 'OE2', 'O', 'C', 'CA', 'N']
    cys = ['CB', 'SG', 'O', 'C', 'CA', 'N']
    asn = ['CB', 'CG', 'OD1', 'ND2', 'O', 'C', 'CA', 'N']

    # Empty matrix
    mtrx = []
    resComp = ('cys', 'glu')
    atom1 = cys[0]




    resComp = ('cys', 'asn')




    resComp = ('glu', 'asn')



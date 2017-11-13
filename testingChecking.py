def main():
    lineIdx = 0
    for line in open('C:/Users/Brianna/PyCharmProjects/research/matching-functions/Motifs/A_1a65_1_10_3_2.py'):
        line = str(line)

        if line[:11] == "cmd.select(" and line.split(",")[1][2] == "n":


            pymol = line.split(",")

            name = ""
            idx = ""
            for c in pymol[0].strip("cmd.select("):
                if ord(c) >= 97:
                    name += c
                elif ord(c) >= 48 and ord(c) <= 57:
                    idx += c


            sele = pymol[1].split("%")
            selection = ((sele[0] + "%" + sele[1]).strip(" '").strip("'")) % float(sele[-1].strip("'(d*").strip("))\n'"))


            data = line[11:-1].split(",")
            parseLine(name=name.upper(), selection=selection, idx=idx)
        lineIdx += 1

def parseLine(name, selection, idx):
    a = 0
    resComp = ()
    sele = selection.split()

    found = "I found ->\n"
    for pie in sele:
        if pie == 'n.' or pie == "'n.":
            a += 1
        elif a == 1:
            if pie[-3:] == '&r.':
                atom1 = pie.strip('&r.')
                found += "\tatom 1 - " + atom1 + ", \n"
            else:
                try:
                    r = float(pie)
                    found += "\tr - " + str(r) + ", \n"
                except:
                    if pie != 'w.' and pie != 'of':
                        res1 = pie.upper()
                        found += "\tres 1 - " + res1 + ",\n"
        elif a == 2:
            if "&" in pie:
                if pie[-3:] == '&r.':
                    atom2 = pie.strip('&r.')
                    found += "\tatom 2 -" + atom2 + ", \n"
                else:
                    second = pie.split("&")

                    atom2 = second[0]
                    res2 = second[1].upper()

                    found += "\tatom 2 -" + atom2 + ",\n\tres2 -" + res2 + "\n\n"
                    if name != res1:
                        resComp = (name, res2)
                    else:
                        resComp = (res1, res2)
            else:
                if pie != 'w.' and pie != 'of':

                    res2 = pie.upper()
                    found += "\tres 2 - " + res2 + "\n\n"
                    if name != res1:
                        resComp = (name, res2)
                    else:
                        resComp = (res1, res2)
    if (res1 == "HIS" and res2 == "HIS") or (res1 == "HISI" and res2 == "HIS") or (res1 == "HISI" or res2 == "HIS") or \
            (res1 == "HISI" and res2 == "HISI"):
        printCombo(resComp, idx, atom1, atom2)

def printCombo(combo, idx, atom1, atom2):
    print "===============< LINE:", idx, ">=================\n"
    print "\tATOM 1: ", atom1
    print "\tATOM 2: ", atom2
    print "\tCOMBO -> ", combo, "\n"

def printPair(atom1, atom2, res1, res2, r, idx):
    print "===============< LINE:", idx, ">================="
    print "\tATOM 1: ", atom1
    print "\tATOM 2: ", atom2
    print "\tRES 1: ", res1
    print "\tRES 2: ", res2
    print "\tR: ", r


if __name__ == '__main__':
    main()
import pandas as pd


def modifyName(res, pair):
    "How many I's? in residue"
    eye = ""
    flag = False

    ra = pair[0][:len(pair[0]) - 1]
    rb = pair[1][:len(pair[1]) - 1]

    for i in range(len(res) - 1, -1, -1):

        if ra + eye == res:
            return ra + eye + pair[0][len(pair[0]) - 1], 0
        elif rb + eye == res:
            return rb + eye + pair[1][len(pair[1]) - 1], 1

        elif res[i] == "I" and flag == False:
            eye += res[i]

        elif res[i] != "I":
            break

    r1 = pair[0][:len(pair[0]) - 1] + eye
    r2 = pair[1][:len(pair[1]) - 1] + eye

    return r1, r2


def buildKey(res1,res2,resPairs):
    """
    Builds key for matrix dictionaries -> accounts for duplicate residues in
    :param res1: res name 1
    :param res2: res name 2
    :param resPairs: list of possible residues for motif file
    :return: tuple containing names of residue 1 and 2 with index
    """
    # print "Res 1: ", res1
    # print "Res 2: ", res2

    # Test cases:
    if res1[-1] != "I" and len(res1) > 3:
        print "What is res1? ", res1
    if res2[-1] != "I" and len(res1) > 3:
        print "What is res2?", res2

    d = {}

    res1_op1 = []
    res1_op2 = []

    res2_op1 = []
    res2_op2 = []


    for pair in resPairs:

        data1 = modifyName(res1, pair)
        data2 = modifyName(res2, pair)

        if isinstance(data1[1], str) and isinstance(data2[1], str):
            r11, r21 = data1
            r12, r22 = data2

            res1_op1.append(r11)
            res1_op2.append(r21)

            res2_op1.append(r12)
            res2_op2.append(r22)

            if res1 == r11 and res2 == r22:
                p1 = r11 + pair[0][len(pair[0]) - 1]
                p2 = r22 + pair[1][len(pair[1]) - 1]
                return (p1, p2)
            elif res1 == r21 and res2 == r12:
                p1 = r21 + pair[1][len(pair[1]) - 1]
                p2 = r12 + pair[0][len(pair[0]) - 1]
                return (p1, p2)

        elif isinstance(data1[1], str):
            r11, r21 = data1
            r2 = data2[0]

            res1_op1.append(r11)
            res1_op2.append(r21)
            res2_op1.append("X")
            res2_op2.append("X")

            if data2[1] == 0:
                if res1 == r21 and res2 == r2:
                    r1 = r21 + pair[1][len(pair[1]) - 1]
                    return (r1, r2)

            elif data2[1] == 1:
                if res1 == r11 and res2 == r2:
                    r1 = r11 + pair[0][len(pair[0]) - 1]
                    return (r1, r2)

        elif isinstance(data2[1], str):
            r1 = data1[0]
            r12, r22 = data2

            res1_op1.append("X")
            res1_op2.append("X")
            res2_op1.append(r12)
            res2_op2.append(r22)

            if data1[1] == 0:
                if res1 == r1 and res2 == r22:
                    r2 = r22 + pair[1][len(pair[1]) - 1]
                    return (r1, r2)

            elif data2[1] == 1:
                if res1 == r1 and res2 == r12:
                    r2 = r12 + pair[0][len(pair[0]) - 1]
                    return (r1, r2)
        else:
            return (data1[0], data2[0])

    d["[R1_O1]"] = res1_op1
    d["[R1_O2]"] = res1_op2
    d["[R2_O1]"] = res2_op1
    d["[R2_O2]"] = res2_op2
    table(d, res1, res2, resPairs)

def table(d, res1, res2, lst):
    tbl = pd.DataFrame(d)
    print "Residues: ", (res1, res2)
    print "From Motif: ", lst
    print tbl
    print "================================"

def main():
    pairs = [('NI1', 'NI2')]
    res1 = "NI"
    res2 = "NI"
    data = buildKey(res1, res2, pairs)

if __name__ == '__main__':
    main()
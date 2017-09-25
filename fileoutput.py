import scipy.misc as sm
import motifFunctions as cmd
global d

def toString(motif, dictionary, name):
    FLAG = True
    idx = 0
    for key in dictionary:
        if name == "comparisons":

                if FLAG == True:
                    motif += name + " = \ \n{" + str(key) + ":\n\t\t" + str(dictionary[key]) + ",\n"
                    FLAG = False
                else:
                    if idx < len(dictionary) - 1:
                        motif += str(key) + ":\n\t\t" + str(dictionary[key]) + ",\n"
                    else:
                        motif += str(key) + ":\n\t\t" + str(dictionary[key]) + "}\n\n"

        elif name == "mtrx":
            if FLAG == True:
                motif += name + " = \ \n{" + str(key) + ":\n\t\t" + str(dictionary[key]) + ",\n"
                FLAG = False
            else:
                if idx < len(dictionary) - 1:
                    motif += str(key) + ":\n\t\t" + str(dictionary[key]) + ",\n"
                else:
                    motif += str(key) + ":\n\t\t" + str(dictionary[key]) + "}\n\n"
        else:
            print "Error or add to method to account to new case."
        idx += 1
    return motif

def tostring(motif, dictionary, name):
    FLAG = True
    idx = 0
    for key in dictionary:
        if name == "comparisons":
            motif += "Comparisons_" + str(key[0]) + "_" + str(key[1]) + " = " + "\n\t\t"
            for row in range(len(dictionary[key])):
                if row < len(dictionary[key]):
                    motif += "\t\t" + str(dictionary[key][row]) + ",\n"
                else:
                    motif += "\t\t" + str(dictionary[key][row]) + "\n\n"
        elif name == "mtrx":
            motif += "Distance_" + str(key[0]) + "_" + str(key[1]) + " = " + "\n\t\t"
            for row in range(len(dictionary[key])):
                if row < len(dictionary[key]):
                    motif += "\t\t" + str(dictionary[key][row]) + ",\n"
                else:
                    motif += "\t\t" + str(dictionary[key][row]) + "\n\n"
                    # motif += "cmd.pca(" + "Distance_" + str(key[0]) + "_" + str(key[1]) + ")\n"

                # if FLAG == True:
                #     motif += name + " = \ \n{" + str(key) + ":\n\t\t" + str(dictionary[key]) + ",\n"
                #     FLAG = False
                # else:
                #     if idx < len(dictionary) - 1:
                #         motif += str(key) + ":\n\t\t" + str(dictionary[key]) + ",\n"
                #     else:
                #         motif += str(key) + ":\n\t\t" + str(dictionary[key]) + "}\n\n"

        elif name == "mtrx":
            if FLAG == True:
                motif += name + " = \ \n{" + str(key) + ":\n\t\t" + str(dictionary[key]) + ",\n"
                FLAG = False
            else:
                if idx < len(dictionary) - 1:
                    motif += str(key) + ":\n\t\t" + str(dictionary[key]) + ",\n"
                else:
                    motif += str(key) + ":\n\t\t" + str(dictionary[key]) + "}\n\n"
        else:
            print "Error or add to method to account to new case."
        idx += 1
    return motif

def parseMotifFiles(newFiles):

    # loop through old motif files
    for file in newFiles:

        # Initialize variables
        filename = ""
        motif = ""
        flag_info = False
        pairs = []
        mtrx = {}
        comparisons = {}
        index = 1

        # loop through lines in motif
        for line in open(file):
            line = str(line)
            # Skip if line consists a delete call
            if line[4:10] == "delete":
                pass

            # Adding Motif Info and creating file name
            elif line.strip("\n") == "'''" and flag_info == True:
                motif += line
                motif += "import motifFunctions as cmd\n"
                flag_info = False

            elif flag_info == True:
                motif += line
                if line[0:4] == "FUNC":
                    filename = line[5:len(line)-1]
                elif line[0:4] == "RESI":
                    res = line[5:].split(",")
                    for _ in range(int(sm.comb(len(res), 2))):
                        pairs.append("")
                        j = 0
            elif line == "'''\n" and flag_info == False:
                motif += line
                flag_info = True


            # Lines that are possible comparisons
            if line[4:10] == "select":
                sele = line.split(",")[1].split("%")
                if len(sele) > 1:

                    if len(sele) != 3:
                        raise Warning

                    selection = ((sele[0] + "%" + sele[1]).strip(" '").strip("'")) %float(sele[-1].strip("'(d*").strip("))\n'"))
                    data = cmd.select(selection=selection, comparisons=comparisons, matrices=mtrx)
                    if data == None:
                        pass
                    else:
                        comparisons, mtrx, resPair, flag = data
                        if flag == True:
                            if resPair not in res:
                                if j == len(res):
                                    raise Warning
                                pairs[j] = resPair
                                j+=1
                            break
            index += 1

        # Pretty print for Printing Distance Matrix
        motif = printMatrices(motif, mtrx, "mtrx")

        # Pretty print for Printing Comparison Matrix
        motif = printMatrices(motif, comparisons, "comparisons")

        """
        Printing as matrices for each pair - > FIX Detect to take in matrices and decide to put in PCA call or to keep it inside of detect
        """

        motif += "cmd.detect(matrices, comparisons)"


        if filename == "" or motif == "":
            print "Didn't create anything"
            raise Warning
        f = open(filename +'.py', 'w')
        f.write(motif)
        f.close()
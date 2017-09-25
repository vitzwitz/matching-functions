import scipy.misc as sm
import motifFunctions as cmd
import os
global d

def MaptoString(motif, distances, comparisons):
    newMaps = []
    for pair in distances:
        newMaps.append(str(pair[0]) + "_" + str(pair[1]))
        motif += str(pair[0]) + "_" + str(pair[1]) + \
                     " = { \n" + "\t'distances'" + ":\n\t\t" + str(distances[pair]) + ",\n"
        motif += "\t'comparisons'" + ":\n\t\t" + str(comparisons[pair]) + "}\n"
    return motif, newMaps


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

        # Convert Comparison and Distance maps into a map for each residue pair:
        #       - key = "distance"   : value = distance matrix
        #       - key = "comparison" : value = comparison matrix
        motif, newMaps = MaptoString(motif, mtrx, comparisons)

        flag = False
        idx = 0
        for pair in newMaps:
            if flag == False:
                motif += "\nmatches = {\n\t\t" + str(str(pair).split("_")) + ": cmd.detect(" + str(pair) + ", d),\n"
                flag = True
            else:
                if idx < len(newMaps)-1:
                    motif += "\t\t" + str(str(pair).split("_")) + ": cmd.detect(" + str(pair) + ", d),\n"
                else:
                    motif += "\t\t" + str(str(pair).split("_")) + ": cmd.detect(" + str(pair) + ", d)}"
            idx += 1


        if filename == "" or motif == "":
            print "Didn't create anything"
            raise Warning

        # Source: https://stackoverflow.com/questions/11700593/creating-files-and-directories-via-python
        path = 'Motifs'
        filename += '.py'
        if not os.path.exists(path):
            os.makedirs(path)

        with open(os.path.join(path, filename), 'wb') as temp_file:
            temp_file.write(motif)

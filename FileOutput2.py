"""
FileOutput2 parses new files to make new adjustments
"""
import os
import scipy.misc as sm


def parseNewMotifFiles(newFiles):
    # loop through old motif files
    for file in newFiles:
        flag = False
        motif = ""
        filename = ""
        count = 0;
        for line in open(file):
            line = str(line)

            if line[:4] == "FUNC":
                filename = line[5:].strip("\n") + ".py"
            # if line[:4] == "RESI":
            #     reS = sm.comb(len(line[5:].split(",")),2)
            #     res = line[5:].split(",")

            if line == "if flag == False:\n":
                motif += line
                flag = True

            # For 1st update
            # elif line == "\tmatches = {\n":
            #     flag = True
            #     motif += line

            elif flag == True:
                if line == "\tmatches = {\n" or\
                line.strip(".py") == "A_135I_3_2_1_17" or\
                line.strip(".py") == "A_132I_3_2_1_17":
                    motif += line
                else:
                    temp = line.strip("").split(":")
                    temp2 = temp[0].strip("\t").split("_")
                    motif += "\t\t'" + temp2[0] + "_" + temp2[1] + "' : " + temp[1]
                    count += 1

            else:
                motif += line


        if filename == "":
            print "Error: Did not find motif name"
            quit()

        if filename[0] != "J":
            # Writes and adds motif file to new directory
            path = 'Motifs_2.0'
            if not os.path.exists(path):
                os.makedirs(path)
            with open(os.path.join(path, filename), 'wb') as temp_file:
                temp_file.write(motif)



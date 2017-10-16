"""
FileOutput2 parses new files to make new adjustments
"""
import os



def parseNewMotifFiles(newFiles):
    # loop through old motif files
    for file in newFiles:
        flag = False
        motif = ""
        filename = ""
        for line in open(file):
            line = str(line)

            if line[:4] == "FUNC":
                filename = line[5:].strip("\n") + ".py"

                #  For first update
                # if filename[0] == "J":
                #     break

            # For 1st update
            # if line[:6] == "\tmatch" and line[6:8] != "es":
            #     splitOld = line.split("=")
            #     motif += splitOld[0] + ", totTime" + str(i) + " =" + splitOld[1]
            #     i += 1
            if line == "matches = {\n":
                motif += "if flag == False:\n"
                motif += "\t" + line
                flag = True

            # For 1st update
            # elif line == "\tmatches = {\n":
            #     flag = True
            #     motif += line
            elif flag == True:
                temp = line.split(":")
                temp2 = temp[0].split("'")
                motif += "\t\t'" + temp2[1] + "_" + temp2[3] + "' : " + temp[1]
            else:
                motif += line


        if filename == "":
            print "Error: Did not find motif name"
            quit()

        if filename[0] != "J":
            # Writes and adds motif file to new directory
            path = 'Motifs'
            if not os.path.exists(path):
                os.makedirs(path)
            with open(os.path.join(path, filename), 'wb') as temp_file:
                temp_file.write(motif)





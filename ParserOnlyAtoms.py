"""
Parser : Inputs and parses pdb files individually
"""
import urllib
from Classes import *

def Constructor(classifier, subfield, line):
    Class = "%s(line)" % classifier
    obj = eval(Class)

    if classifier not in subfield:
        subfield[classifier] = [obj]
    else:
        subfield[classifier].append(obj)
    return subfield, obj


def readFile(file):

    AtomsNModels = {}
    min = (0, 0, 0)
    i = 1
    for line in open(file).readlines():
        line = str(line.rstrip())
        if line == "": pass
        classifier = line[0:6]
        # if i == 19: break
        if line[0:6] == "SPRSDE":
            pass
        else:
            classifier = classifier[0] + classifier[1:].lower()
            classifier = classifier.strip()

        if classifier == 'Atom':
            AtomsNModels, obj = Constructor(classifier, AtomsNModels, line)

        else:
            pass
        i += 1

    return AtomsNModels


def main():
    # For Testing:
    pdbID = raw_input("Enter a pdb code: ")
    directory = "C:/Users/blm7643/Downloads/proteinDATA/"
    path = urllib.urlretrieve('http://files.rcsb.org/download/%s.pdb' % pdbID,
                              'C:/Users/blm7643/Downloads/proteinDATA/%s.pdb' % pdbID)
    file = 'C:/Users/blm7643/Downloads/proteinDATA/%s.pdb' % pdbID
    pdb = readFile(file)


if __name__ == '__main__':
    main()
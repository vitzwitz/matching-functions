"""
Parser : Inputs and parses pdb files individually

"""
from Classes import *
import urllib, urllib2

def Constructor(classifier, subfield, line):
    Class = "%s(line)" % classifier
    print classifier
    obj = eval(Class)
    print "Works!"
    print obj
    if classifier not in subfield:
        subfield[classifier] = [obj]
    else:
        subfield[classifier].append(obj)
    return subfield


def readFile(file):

    description     = {}
    primaryStruct   = {}
    heterogen       = {}
    secondaryStruct = {}
    sites           = {}
    coordTransf     = {}
    AtomsNModels          = {}
    connectivity    = {}
    bookskeeping    = {}
    i = 1
    for line in open(file).readlines():
        line = str(line.rstrip())
        if line == "": pass
        classifier = line[0:6]
        #if i == 19: break
        if line[0:6] == "SPRSDE":
            pass
        else:
            classifier = classifier[0] + classifier[1:].lower()
            classifier = classifier.strip()
        print i, classifier  # line piece

        if classifier == 'Header' or classifier == "Title" or classifier == 'Source' \
        or classifier == 'Author' or classifier == 'Remark' or classifier == "Obslte" \
        or classifier == "Caveat" or classifier == "Split" or classifier == "SPRSDE" \
        or classifier == "Expdta" or classifier == "Revdat" or classifier == 'Keywds' \
        or classifier == 'Jrnl':
                description = Constructor(classifier, description, line)
        elif classifier == 'Compnd':
                description = Constructor("Compound", description, line)
        elif classifier == 'Nummdl':
                description = Constructor("NumModels", description, line)
        elif classifier == 'Modltyp':
                description = Constructor("ModelType", description, line)


        elif classifier == 'Dbref':
                primaryStruct = Constructor((classifier[0] + classifier[1:3].upper() + classifier[4:6]),
                                            primaryStruct, line)
        elif classifier == 'Seqres' or classifier == "Modres" or classifier == "Seqadv":
                primaryStruct = Constructor((classifier[0:3] + classifier[3].upper() + classifier[4:6]),
                                            primaryStruct, line)

        elif classifier == 'Het' or classifier == 'Formul':
                heterogen = Constructor(classifier, heterogen, line)
        elif classifier == 'Hetnam':
                heterogen = Constructor("HetCompound", heterogen, line)
        elif classifier == 'Hetsyn':
                heterogen = Constructor("HetSynon", heterogen, line)


        elif classifier == 'Helix' or classifier == 'Sheet' or \
                            classifier == "Turn":
                secondaryStruct = Constructor(classifier, secondaryStruct, line)


        elif classifier == 'Ssbond':
                connectivity = Constructor("S2Bond", connectivity, line)
        elif classifier == 'Link':
                connectivity = Constructor(classifier, connectivity, line)
        elif classifier == "Cispep":
                connectivity = Constructor("CisPep", connectivity, line)

        elif classifier == 'Site':
                sites = Constructor(classifier, sites, line)

        elif classifier == 'Cryst1' or classifier == 'Scale1' or \
                            classifier == Scale2 or classifier == Scale3:
                coordTransf = Constructor(classifier, coordTransf, line)
        elif classifier == 'ORIGX1' or classifier == 'ORIGX2' or \
                            classifier == 'ORIGX3':
                coordTransf = Constructor(classifier[0:4] + classifier[4].upper()+classifier[5], coordTransf, line)
        elif classifier == 'Mtrix1' or classifier == 'Mtrix2' or classifier == 'Mtrix3':
                coordTransf = Constructor(classifier[0]+"a"+classifier[1:], coordTransf, line)
        elif classifier == "Tvect":
                coordTransf = Constructor("TVector", coordTransf, line)


        elif classifier == 'Atom' or classifier == "Anisou" or classifier == 'Ter' \
                    or classifier == Model:
                AtomsNModels= Constructor(classifier, AtomsNModels, line)
        elif classifier == 'Hetatm':
                AtomsNModels= Constructor("HetAtom", AtomsNModels, line)
        elif classifier == "Hydbnd":
                AtomsNModels= Constructor("HydroBond", AtomsNModels, line)
        elif classifier == "Sltbdg":
                AtomsNModels= Constructor("SaltBridge", AtomsNModels, line)
        elif classifier == "Endmdl":
                AtomsNModels= Constructor("EndModel", AtomsNModels, line)

        elif classifier == 'Conect':
                connectivity = Constructor("Connects", connectivity, line)

        elif classifier == 'Master' or classifier == "End":
                bookskeeping = Constructor(classifier, bookskeeping, line)
        else:
            print "other =", classifier
        i += 1

    
    pdb = (description, primaryStruct, heterogen, secondaryStruct, sites, coordTransf, AtomsNModels, connectivity, bookskeeping)
    return pdb




def main():
    # For Testing:
    pdbID = raw_input("Enter a pdb code: ")
    directory = "C:/Users/blm7643/Downloads/proteinDATA/"
    path = urllib.urlretrieve('http://files.rcsb.org/download/%s.pdb' % pdbID, 'C:/Users/blm7643/Downloads/proteinDATA/%s.pdb' % pdbID)
    file = 'C:/Users/blm7643/Downloads/proteinDATA/%s.pdb' % pdbID
    pdb = readFile(file)

if __name__ == '__main__':
    main()
import functions as f
import ParserOnlyAtoms as poa
import fileoutput as fo
import os
import motifFunctions as cmd
import threading


# import Classes as cl
# # import kdtreeCOPY as kdc
# import kdtree4atoms as kdt
# import time as t
# import numpy as np

def testDistBasedCluster():
    # For categorizing all points
    pdbID = raw_input("Enter a pdb code: ")
    path = poa.urllib.urlretrieve('http://files.rcsb.org/download/%s.pdb' % pdbID,
                              'C:/Users/Brianna/Downloads/proteinDATA/%s.pdb' % pdbID)
    try:
        file = 'C:/Users/blm7643/Downloads/proteinDATA/%s.pdb' % pdbID
        pdbData = poa.readFile(file)
    except IOError:
        file = '%s.pdb' % pdbID
        pdbData = poa.readFile(file)

    Clusters = {}
    Atoms = pdbData["Atom"]
    ptr = Atoms[0]
    r = 0.5
    # K = 10
    print "Atoms:", len(Atoms)

    cluster, other, flag = f.createClusterbasedonDistance(r, ptr, Atoms)  # First Cluster
    Clusters[ptr, r] = cluster  # First cluster stored
    curr = other  # Temp other
    # while len(cluster) != len(Atoms):
    while curr != []:
        r += r  # New Class
        cluster, other, flag = f.createClusterbasedonDistance(r, ptr, curr)  # New Cluster
        Clusters[r] = cluster  # Store Cluster
        curr = other

def testBasicDistCluster():
    # For finding atoms within a distance of a point
    pdbID = raw_input("Enter a pdb code: ")
    path = poa.urllib.urlretrieve('http://files.rcsb.org/download/%s.pdb' % pdbID,
                              'C:/Users/Brianna/Downloads/proteinDATA/%s.pdb' % pdbID)
    try:
        file = 'C:/Users/blm7643/Downloads/proteinDATA/%s.pdb' % pdbID
        pdbData = poa.readFile(file)
    except IOError:
        file = '%s.pdb' % pdbID
        pdbData = poa.readFile(file)

    Clusters = {}
    Atoms = pdbData["Atom"]
    ptr = Atoms[0]
    r = 0.5
    # K = 10        # Limit cluster size ? If
    print "Atoms:", len(Atoms)

    cluster, other, flag = f.createClusterbasedonDistance(r, ptr, Atoms)  # First Cluster
    Clusters[ptr, r] = cluster  # First cluster stored
    curr = other  # Temp other
    # while len(cluster) != len(Atoms):
    while curr != []:
        r += r  # New Class
        cluster, other, flag = f.createClusterbasedonDistance(r, ptr, curr)  # New Cluster
        Clusters[r] = cluster  # Store Cluster
        curr = other

def testKBasedCluster():
    # For Testing:
        pdbID = raw_input("Enter a pdb code: ")
        path = poa.urllib.urlretrieve('http://files.rcsb.org/download/%s.pdb' % pdbID,
                                  'C:/Users/Brianna/Downloads/proteinDATA/%s.pdb' % pdbID)
        try:
            file = 'C:/Users/blm7643/Downloads/proteinDATA/%s.pdb' % pdbID
            pdbData = poa.readFile(file)
        except IOError:
            file = '%s.pdb' % pdbID
            pdbData = poa.readFile(file)

        Atoms = pdbData["Atom"]
        ptr = Atoms[0]
        K = 10
        nearestNeighbors = f.createClusterBasedonK(ptr, Atoms, K)

        for neighbor in nearestNeighbors:
            print neighbor.name

def testkNN_w_inDistance():
    # For Testing:
    pdbID = raw_input("Enter a pdb code: ")
    path = poa.urllib.urlretrieve('http://files.rcsb.org/download/%s.pdb' % pdbID,
                              'C:/Users/Brianna/Downloads/proteinDATA/%s.pdb' % pdbID)
    try:
        file = 'C:/Users/blm7643/Downloads/proteinDATA/%s.pdb' % pdbID
        pdbData = poa.readFile(file)
    except IOError:
        file = '%s.pdb' % pdbID
        pdbData = poa.readFile(file)

    Atoms = pdbData["Atom"]
    ptr = Atoms[0]
    K = 10
    distance = 10
    nearestNeighbors = f.kNN_wDistance(ptr, Atoms, K, distance)


def testingKNN_specificAtoms():
    pdbID = raw_input("Enter a pdb code: ")
    path = poa.urllib.urlretrieve('http://files.rcsb.org/download/%s.pdb' % pdbID,
                              'C:/Users/Brianna/Downloads/proteinDATA/%s.pdb' % pdbID)
    try:
        file = 'C:/Users/blm7643/Downloads/proteinDATA/%s.pdb' % pdbID
        pdbData = poa.readFile(file)
    except IOError:
        file = '%s.pdb' % pdbID
        pdbData = poa.readFile(file)

    Atoms = pdbData["Atom"]
    desiredAtoms = f.getSpecificAtom("CB", "GLU", Atoms)

    distance = 11.14
    constraint = ["SG", "CB", "CA", "C", "N", "O"]
    constraint.sort()
    K = len(constraint)

    for CB in desiredAtoms:
        neighbors, walking = f.kNN_resNames(Atoms, K, distance, CB, "CYS")
        if len(neighbors) == K:
            neighbors.sort()
            if neighbors == constraint:
                print CB.serial, CB.resSeq, ":", neighbors
                print walking

def main():
        # pdbID = raw_input("Enter a pdb code: ")
        # pdbID = '1a0j'
        # path = poa.urllib.urlretrieve('http://files.rcsb.org/download/%s.pdb' % pdbID,
        #                           'C:/Users/Brianna/PycharmProjects/ClusterAlg/%s.pdb' % pdbID)
        # try:
        #     file = 'C:/Users/blm7643/Downloads/proteinDATA/%s.pdb' % pdbID
        #     pdbData = poa.readFile(file)
        # except IOError:
        #     file = '%s.pdb' % pdbID
        #     pdbData = poa.readFile(file)
        #
        # # start = t.time()
        # Atoms = pdbData["Atom"]
        # TREE = kdt.KDTree4Atoms(np.asarray(Atoms))


        # treeTime = t.time() - start
        # desiredAtoms = getSpecificAtom("CB", "GLU", Atoms)

        " Testing query"
        # neighs = tree.query(desiredAtoms[0], k=3, res="CYS")
        # for ne in neighs:
        #     print ne.resName
        # neighs = tree.query(desiredAtoms[0], res="CYS", atomName="SG")
        # print("===================")
        # neighss = tree.query(desiredAtoms[0], res="ASN", atomName="SG")

        " Testing query_ball_poiint"
        # print desiredAtoms[0].position
        # neighs1 = tree.query_ball_point(desiredAtoms[0], 9.0, eps=0, res="GLU")
        # print len(neighs1), "\n", neighs1
        # neighs2 = tree.query_ball_point(desiredAtoms[0], 9.0, eps=0, res="ALA")
        # print len(neighs2), "\n", neighs2

        "Testing query_pairs"
        # startQuery = t.time()
        # cmd.select('cys5', 'n. CB&r. cys w. %s of n. OE2&r. glu'%(d*10.70))
        # neighS = treee.query_pairs(r=10.70, res1="CYS", res2="GLU", atomName1="CB", atomName2="OE2")
        # queryyy = t.time() - startQuery
        # print neighS
        # print len(neighS)
        # print("Building Tree:", treeeeee, "seconds")
        # print("Motifing:", queryyy, "seconds")
        # print("**********************************************************************************")
        # neighB = treee.query_pairs(r=20., res1="CYS", res2="GLU", atomName1="CB", atomName2="OE2")
        # print neighB
        # print len(neighB)

        "Testing query_pairs that uses query"
        # atom1 = "CB"
        # res1 = "CYS"
        # r = [8.79,9.87,9.67,8.65,10.70,8.10,8.26,9.12,10.47]
        # atomSet = ['CB','CG','CD','OE1','OE2','O','C','CA', 'N']
        # res2 = "GLU"
        # sTart = t.time()
        # results = treee.query_pairs(r, res1, atom1, res2, atomSet)
        # wRes = t.time() - sTart
        # print "time", wRes
        # # results = [(name, Atoms[i]) for (name,i) in indices]
        #
        # print(results)
        # # for rslt in results:
        #     print "Actual Atom name:", rslt[0], "Exp Atom Name:", Atoms[rslt[1]], "index:", rslt[1]

        "Testing Motif with Query Pairs + Query"
        # execfile("A_1a4s_1_2_1_8.txt")

        "Testing distance matrix builder"
        # execfile("motifTester1.py")


        "Testing Motif Parser with test File"
        # fo.parseMotifFiles(["MotifParserTest1.py"])

        "Testing Motif Parser with Directory"
        # Source : https://stackoverflow.com/questions/19587118/iterating-through-directories-with-python

        # rootdir = 'C:/Users/Brianna/PyCharmProjects/optimizer/OldMotifs'
        #
        # motifFiles = []
        # for subdir, dirs, files in os.walk(rootdir):
        #     for file in files:
        #         motifFiles.append(os.path.join(subdir, file))
        # fo.parseMotifFiles(motifFiles)

        "Testing PCA & looping through a list of motif files "
        # path = 'C:/Users/Brianna/PyCharmProjects/research/matching-functions/Motifs'
        # motifs = []
        # for subdir, dirs, files in os.walk(path):
        #     for file in files:
        #         motifs.append(os.path.join(subdir, file))
        #
        # i = 1
        # for motif in motifs:
        #     execfile(motif)
        #     i += 1

        "Creating File of Motif Names"
        # path_data = 'C:/Users/Brianna/PyCharmProjects/optimizer/Data'
        # motifNames = ""
        # for subdir, dirs, files in os.walk(path):
        #     for file in files:
        #         motifNames += file.strip(".py") + "\n"
        #
        # if not os.path.exists(path_data):
        #     os.makedirs(path_data)
        # with open(os.path.join(path_data, "motifNames.txt"), 'wb') as temp_file:
        #     temp_file.write(motifNames)


        "Visualizing Data"
        # execfile("Motifs/A_1a4s_1_2_1_8.py")

        "Testing family of proteins w/ all proteins & put data in files"
        # path = 'C:/Users/Brianna/PyCharmProjects/research/matching-functions/Motifs'
        # motifs = []
        # for subdir, dirs, files in os.walk(path):
        #     for file in files:
        #         motifs.append(os.path.join(subdir, file))
        #
        # i = 1
        # for motif in motifs:
        #     print "Testing motif " + str(i) + "..."
        #     execfile(motif)
        #     i+=1
        #     print "Done!"


        "Fixing Motif File Bug -> i = 7, A_1a65_1_10_3_2"
        #

        # rootdir = 'C:/Users/Brianna/PyCharmProjects/optimizer/Motifs'
        #
        # motifFiles = []
        # for subdir, dirs, files in os.walk(rootdir):
        #     for file in files:
        #         motifFiles.append(os.path.join(subdir, file))
        # fo2.parseNewMotifFiles(motifFiles)


        " Fix Motif files -> typo; re-parsed"
        # Edge case : residue having 1 atom

        # rootdir = 'C:/Users/Brianna/PyCharmProjects/optimizer/UpdatedMotifs'
        #
        # motifFiles = []
        # for subdir, dirs, files in os.walk(rootdir):
        #     for file in files:
        #         motifFiles.append(os.path.join(subdir, file))
        # fo2.parseNewMotifFiles(motifFiles)

        "Fixing another bug in motifs -> i = 1, A_1a0j_3_4_21_4"
        # misusing parameter ->
        #   REMINDER : add atom 1 & atom 2 as parameters in storeData

        # execfile("Motifs/A_1a0j_3_4_21_4.py")


        " Fix 2nd Motif File Bug i = 16 -> A_1afw_2_3_1_16"
        # Residue pair of the same residue name and same structure & one atom inside -> cluster : res1 == res2  &&  atom1 == [atom2]
        # execfile("Motifs/A_1afw_2_3_1_16.py")

        "Fixing motif : i = 24, A_1am2_5_99_1_3 "
        # TypeError : unsupported list & long for division -> not converting mtrx & its rows to np.ndarrays
            # execfile("Motifs/A_1am2_5_99_1_3.py")

        # Uneven matrices -> source? bug in fileoutput

        # Redo all files
        # rootdir = 'C:/Users/Brianna/PyCharmProjects/research/matching-functions/Motifs'
        #
        # motifFiles = []
        # for subdir, dirs, files in os.walk(rootdir):
        #     for file in files:
        #         motifFiles.append(os.path.join(subdir, file))
        # fo.parseMotifFiles(motifFiles)

        # Redo update
        # rootdir = 'C:/Users/Brianna/PyCharmProjects/research/matching-functions/Motifs_old'

        # motifFiles = []
        # for subdir, dirs, files in os.walk(rootdir):
        #     for file in files:
        #         motifFiles.append(os.path.join(subdir, file))
        # fo2.parseNewMotifFiles(motifFiles)

        "Testing All Motifs with 2 pdb structures -> bugs fixed in parsing functions"
        path = 'C:/Users/Brianna/PyCharmProjects/research/matching-functions/Motif_2.0'
        # motifs = []
        # for subdir, dirs, files in os.walk(path):
        #     for file in files:
        #         motifs.append(os.path.join(subdir, file))
        #
        # i = 1
        # for motif in motifs:
        #     print "Testing motif " + str(i) + "..."
        #     execfile(motif)
        #     i+=1
        #     print "Done!"

        "Re-occured bug -> key is not str in matches structure at end of motif file"

        # rootdir = 'C:/Users/Brianna/PyCharmProjects/research/matching-functions/Motif_2.0'
        # motifFiles = []
        # for subdir, dirs, files in os.walk(rootdir):
        #     for file in files:
        #         motifFiles.append(os.path.join(subdir, file))
        # fo2.parseNewMotifFiles(motifFiles)

        " Minor adjustments: Add missing tab, Remove if statement, Remove tab"

        # rootdir = 'C:/Users/Brianna/PyCharmProjects/research/matching-functions/Motif_2.0'
        # motifFiles = []
        # for subdir, dirs, files in os.walk(rootdir):
        #     for file in files:
        #         motifFiles.append(os.path.join(subdir, file))
        # fo2.parseNewMotifFiles(motifFiles)

        " Minor adjustments: (Hard-coded) removed from A_132l_3_2_1_17 & A_135l_3_2_1_17 "
        # (Hard-coded)

        " Bug -> duplicate residues, ill-produced matrices -> Residues that end in i -> Residues that end with " \
        "multiple I's (part of A's), Res Pairs that both end in I's (in M's) -> Take I's properly & Metal Res names" \
        " (in R's) -> Residues that end in I -> Parsing Part 1 successful -> Motifs with 2 residues -> Added lines twice" \
        "-> FIXED"

        # rootdir = 'C:/Users/Brianna/PyCharmProjects/research/matching-functions/Motifs_2.0'
        # motifFiles = []
        # for subdir, dirs, files in os.walk(rootdir):
        #     for file in files:
        #         motifFiles.append(os.path.join(subdir, file))
        #
        # fo.parsePart3(motifFiles)


        # Redo all files
        rootdir = '/home/michael/Documents/Git/bris_research/research/matching-functions-master/Motifs'

        motifFiles = []
        for subdir, dirs, files in os.walk(rootdir):
            for file in files:
                motifFiles.append(os.path.join(subdir, file))

        # fo.parseMotifFiles(motifFiles)
        #
        # # Redo update
        rootdir = '/home/michael/Documents/Git/bris_research/research/matching-functions-master/Motifs_old'

        motifFiles = []
        for subdir, dirs, files in os.walk(rootdir):
            for file in files:
                motifFiles.append(os.path.join(subdir, file))

        # fo.parseNewMotifFiles(motifFiles)



        # rootdir = 'C:/Users/Brianna/PyCharmProjects/research/Motifs'
        #
        # motifFiles = []
        # for subdir, dirs, files in os.walk(rootdir):
        #     for file in files:
        #         motifFiles.append(os.path.join(subdir, file))
        # data = fo.checkLines(motifFiles)
        #
        # files = data[1]
        #
        # print "==============  Table  ==============="
        # print data[0]
        # print "==============  Files  ==============="
        # for i in range(0,len(files), 8):
        #     print files[i], "|||", files[i+1], "|||",files[i+2], "|||", files[i+3], "|||", files[i+4], "|||",files[i+5], "|||", files[i+6], "|||", files[i+7]

        "Testing all Motifs Again"

        # path = 'C:/Users/Brianna/PyCharmProjects/research/matching-functions/Motifs_2.1'
        # motifs = []
        # for subdir, dirs, files in os.walk(path):
        #     for file in files:
        #         motifs.append(os.path.join(subdir, file))
        #
        # i = 1
        # for motif in motifs:
        #     print "Testing motif " + str(i) + "..."
        #     execfile(motif)
        #     i+=1
        # print "Done!"

        " Removed old method to deal with residue pairs -> now append pairs to list along the way & modify the" \
        " key by comparing the current pair with that list "

        # Motifs that fail main tests but seem fine -> PROBLEM : SAME NAME , SAME KEY -> map will add it to old one
        # checkLater = ["A_1a65_1_10_3_2"]



        """
        ISSUES FACED ->
            1. Multiple of same residue names
            2. only 2 residues
            3. 2 total type & duplicates of at least one


        MOTIFS THAT CAUSED PROBLEMS ->
            1. A_1a50_4_2_1_20, A_1a65_1_10_3_2,
            2. A_135l_3_2_1_17, A_132l_3_2_1_17,
            3. A_1cwy_2_4_1_25


        NOTE ->  Doesn't save all orientations for pairs... if it is problem 3 ***

        Instead of fixing during initial parsing, fix during 4th parsing

            loop thru file & if matrices are ill-formed, split into new maps
        """

        rootdir = '/home/michael/Documents/Git/bris_research/research/matching-functions/Motifs_2.0'

        motifFiles = []
        for subdir, dirs, files in os.walk(rootdir):
            for file in files:
                motifFiles.append(os.path.join(subdir, file))

        for motifFile in motifFiles:
            fo.fixingPairStructuresInFiles(motifFile)

        # threads = []
        # for motifFile in motifFiles:
        #     t = threading.Thread(target=fo.fixingPairStructuresInFiles, args=(motifFile,))
        #     threads.append(t)
        #     t.start()


        # "Testing : str distances matrix -> float matrix"
        # # Test 1. Normal matrix
        # ad = "		[[11.72, 10.79, 10.06, 11.03], [12.61, 11.73, 11.12, 11.85], [13.78, 12.93, 12.29, 13.08], [12.27, 11.39, 10.94, 11.39]],"
        # ad = ad.strip()
        # # A = cmd.strTomatrix(a, "distances")
        # # print "Test 1 <Normal Matrix>", A
        #
        # # Test 2. One row
        # bd = "		[17.8, 18.48, 17.67, 16.53, 16.74, 18.0, 15.78],"
        # bd = bd.strip()
        # # B = cmd.strTomatrix(b, "distances")
        # # print "Test 2 <One Row>", B
        #
        # # Test 3. One column
        # cd = "		[[9.01], [8.01], [6.58], [6.2], [6.18], [13.39], [12.24], [11.04], [10.61], [10.72]],"
        # cd = cd.strip()
        # # C = cmd.strTomatrix(c, "distances")
        # # print "Test 3 <One Column>", C
        #
        # # Test 4. One element
        # dd = "		[6.9],"
        # dd = dd.strip()
        # # D = cmd.strTomatrix(d, "distances")
        # # print "Test 4 <One element>", D
        #
        #
        # # Test 1. Normal matrix
        # ac = "		[[('CB', 'ASP', 'CB', 'ASP', 11.72), ('CB', 'ASP', 'CG', 'ASP', 12.61), ('CB', 'ASP', 'OD1', 'ASP', 13.78), ('CB', 'ASP', 'OD2', 'ASP', 12.27)], [('CG', 'ASP', 'CB', 'ASP', 10.79), ('CG', 'ASP', 'CG', 'ASP', 11.73), ('CG', 'ASP', 'OD1', 'ASP', 12.93), ('CG', 'ASP', 'OD2', 'ASP', 11.39)], [('OD1', 'ASP', 'CB', 'ASP', 10.06), ('OD1', 'ASP', 'CG', 'ASP', 11.12), ('OD1', 'ASP', 'OD1', 'ASP', 12.29), ('OD1', 'ASP', 'OD2', 'ASP', 10.94)], [('OD2', 'ASP', 'CB', 'ASP', 11.03), ('OD2', 'ASP', 'CG', 'ASP', 11.85), ('OD2', 'ASP', 'OD1', 'ASP', 13.08), ('OD2', 'ASP', 'OD2', 'ASP', 11.39)]]}"
        # ac = ac.strip()
        # A = cmd.strTomatrix(ac, ad)
        # print "Test 1 <Normal Matrix>"
        # cmd.printMatrix(A[0])
        # cmd.printMatrix(A[1])
        #
        # # Test 2. One row
        # bc = "		[('MG', 'MG', 'CB', 'ARG', 17.8), ('MG', 'MG', 'CG', 'ARG', 18.48), ('MG', 'MG', 'CD', 'ARG', 17.67), ('MG', 'MG', 'NE', 'ARG', 16.53), ('MG', 'MG', 'CZ', 'ARG', 16.74), ('MG', 'MG', 'NH1', 'ARG', 18.0), ('MG', 'MG', 'NH2', 'ARG', 15.78)]}"
        # bc.strip()
        # B = cmd.strTomatrix(bc, bd)
        # print "Test 2 <One Row>"
        # cmd.printMatrix(B[0])
        # cmd.printMatrix(B[1])
        #
        # # Test 3. One column
        # cc = "		[[('CB', 'GLU', 'MG', 'MG', 9.01)], [('CG', 'GLU', 'MG', 'MG', 8.01)], [('CD', 'GLU', 'MG', 'MG', 6.58)], [('OE1', 'GLU', 'MG', 'MG', 6.2)], [('OE2', 'GLU', 'MG', 'MG', 6.18)], [('CB', 'GLU', 'MG', 'MG', 13.39)], [('CG', 'GLU', 'MG', 'MG', 12.24)], [('CD', 'GLU', 'MG', 'MG', 11.04)], [('OE1', 'GLU', 'MG', 'MG', 10.61)], [('OE2', 'GLU', 'MG', 'MG', 10.72)]]}"
        # cc.strip()
        # C = cmd.strTomatrix(cc, cd)
        # print "Test 3 <One Column>"
        # cmd.printMatrix(C[0])
        # cmd.printMatrix(C[1])
        #
        # # Test 4. One element
        # dc = "		[('MG', 'MG', 'MG', 'MG', 6.9)]}"
        # dc.strip()
        # D = cmd.strTomatrix(dc, dd)
        # print "Test 4 <One element>"
        # cmd.printMatrix(D[0])
        # cmd.printMatrix(D[1])

if __name__ == '__main__':

    global d
    d = 1.0
    main()
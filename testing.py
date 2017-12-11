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


        # # Redo all files
        # rootdir = 'C:/Users/Brianna/PyCharmProjects/research/matching-functions/Motifs'
        #
        # motifFiles = []
        # for subdir, dirs, files in os.walk(rootdir):
        #     for file in files:
        #         motifFiles.append(os.path.join(subdir, file))
        #
        # fo.parseMotifFiles(motifFiles)
        #
        # # Redo update
        #
        # rootdir = 'C:/Users/Brianna/PyCharmProjects/research/matching-functions/Motifs_old'
        #
        # motifFiles = []
        # for subdir, dirs, files in os.walk(rootdir):
        #     for file in files:
        #         motifFiles.append(os.path.join(subdir, file))
        #
        # fo.parseNewMotifFiles(motifFiles)



        # rootdir = 'C:/Users/Brianna/PyCharmProjects/research/Motifs'
        #
        # motifFiles = []
        # for subdir, dirs, files in os.walk(rootdir):
        #     for file in files:
        #         motifFiles.append(os.path.join(subdir, file))
        #
        # data = fo.checkLines(motifFiles)
        #
        # files = data[1]
        #
        # print "==============  Table  ==============="
        # print data[0]
        # print "==============  Files  ==============="
        # for i in range(0,len(files), 8):
        #     print files[i], "|||", files[i+1], "|||",files[i+2], "|||", files[i+3], "|||", files[i+4], "|||",files[i+5], "|||", files[i+6], "|||", files[i+7]

        # "Testing all Motifs Again"

        path = 'C:/Users/Brianna/PyCharmProjects/research/matching-functions/Motifs_3.0'
        motifs = []
        for subdir, dirs, files in os.walk(path):
            for file in files:
                motifs.append(os.path.join(subdir, file))

        i = 1
        for motif in motifs:
            print "Testing motif " + str(i) + "..."
            execfile(motif)
            i+=1
        print "Done!"

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

        # rootdir = '/home/michael/Documents/Git/bris_research/research/matching-functions/Motifs_2.0'
        # rootdir = 'C:/Users/Brianna/PycharmProjects/research/matching-functions/Motifs_2.0'
        #
        # motifFiles = []
        # for subdir, dirs, files in os.walk(rootdir):
        #     for file in files:
        #         motifFiles.append(os.path.join(subdir, file))
        #
        # for motifFile in motifFiles:
        #     fo.fixingPairStructuresInFiles(motifFile)

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


        # Testing

        # TEST 1: Normal Matrix - from A_1a50_4_2_1_20 (his,lys,lys,asp)

        # motif = ""
        # filename = 'A_1a50_4_2_1_20'
        # total_pairs = []
        # pair = 'LYS_ASP'
        # updated_map = {}
        #
        # updated_map['distances']   = [[15.95, 14.68, 13.61, 14.86, 17.13, 16.13, 15.93, 14.9],
        #                               [14.57, 13.35, 12.25, 13.6, 15.75, 14.71, 14.5, 13.43],
        #                               [13.58, 12.28, 11.25, 12.42, 14.9, 13.91, 13.66, 12.68],
        #                               [12.13, 10.86, 9.79, 11.08, 13.41, 12.4, 12.15, 11.17],
        #                               [11.76, 10.61, 9.54, 10.93, 13.22, 12.14, 11.72, 10.6],
        #                               [18.62, 17.33, 16.23, 17.49, 19.49, 18.54, 18.54, 17.58],
        #                               [18.32, 17.05, 15.96, 17.24, 19.34, 18.35, 18.24, 17.21],
        #                               [17.07, 15.85, 14.73, 16.11, 18.11, 17.08, 16.93, 15.85],
        #                               [17.32, 16.18, 15.06, 16.5, 18.47, 17.38, 17.12, 15.95]]
        #
        # updated_map['comparisons'] = [[('CB', 'LYS', 'CB', 'ASP', 15.95), ('CB', 'LYS', 'CG', 'ASP', 14.68), ('CB', 'LYS', 'OD1', 'ASP', 13.61), ('CB', 'LYS', 'OD2', 'ASP', 14.86), ('CB', 'LYS', 'O', 'ASP', 17.13), ('CB', 'LYS', 'C', 'ASP', 16.13), ('CB', 'LYS', 'CA', 'ASP', 15.93), ('CB', 'LYS', 'N', 'ASP', 14.9)],
        #                              [('CG', 'LYS', 'CB', 'ASP', 14.57), ('CG', 'LYS', 'CG', 'ASP', 13.35), ('CG', 'LYS', 'OD1', 'ASP', 12.25), ('CG', 'LYS', 'OD2', 'ASP', 13.6), ('CG', 'LYS', 'O', 'ASP', 15.75), ('CG', 'LYS', 'C', 'ASP', 14.71), ('CG', 'LYS', 'CA', 'ASP', 14.5), ('CG', 'LYS', 'N', 'ASP', 13.43)],
        #                              [('CD', 'LYS', 'CB', 'ASP', 13.58), ('CD', 'LYS', 'CG', 'ASP', 12.28), ('CD', 'LYS', 'OD1', 'ASP', 11.25), ('CD', 'LYS', 'OD2', 'ASP', 12.42), ('CD', 'LYS', 'O', 'ASP', 14.9), ('CD', 'LYS', 'C', 'ASP', 13.91), ('CD', 'LYS', 'CA', 'ASP', 13.66), ('CD', 'LYS', 'N', 'ASP', 12.68)],
        #                              [('CE', 'LYS', 'CB', 'ASP', 12.13), ('CE', 'LYS', 'CG', 'ASP', 10.86), ('CE', 'LYS', 'OD1', 'ASP', 9.79), ('CE', 'LYS', 'OD2', 'ASP', 11.08), ('CE', 'LYS', 'O', 'ASP', 13.41), ('CE', 'LYS', 'C', 'ASP', 12.4), ('CE', 'LYS', 'CA', 'ASP', 12.15), ('CE', 'LYS', 'N', 'ASP', 11.17)],
        #                              [('NZ', 'LYS', 'CB', 'ASP', 11.76), ('NZ', 'LYS', 'CG', 'ASP', 10.61), ('NZ', 'LYS', 'OD1', 'ASP', 9.54), ('NZ', 'LYS', 'OD2', 'ASP', 10.93), ('NZ', 'LYS', 'O', 'ASP', 13.22), ('NZ', 'LYS', 'C', 'ASP', 12.14), ('NZ', 'LYS', 'CA', 'ASP', 11.72), ('NZ', 'LYS', 'N', 'ASP', 10.6)],
        #                              [('O', 'LYS', 'CB', 'ASP', 18.62), ('O', 'LYS', 'CG', 'ASP', 17.33), ('O', 'LYS', 'OD1', 'ASP', 16.23), ('O', 'LYS', 'OD2', 'ASP', 17.49), ('O', 'LYS', 'O', 'ASP', 19.49), ('O', 'LYS', 'C', 'ASP', 18.54), ('O', 'LYS', 'CA', 'ASP', 18.54), ('O', 'LYS', 'N', 'ASP', 17.58)],
        #                              [('C', 'LYS', 'CB', 'ASP', 18.32), ('C', 'LYS', 'CG', 'ASP', 17.05), ('C', 'LYS', 'OD1', 'ASP', 15.96), ('C', 'LYS', 'OD2', 'ASP', 17.24), ('C', 'LYS', 'O', 'ASP', 19.34), ('C', 'LYS', 'C', 'ASP', 18.35), ('C', 'LYS', 'CA', 'ASP', 18.24), ('C', 'LYS', 'N', 'ASP', 17.21)],
        #                              [('CA', 'LYS', 'CB', 'ASP', 17.07), ('CA', 'LYS', 'CG', 'ASP', 15.85), ('CA', 'LYS', 'OD1', 'ASP', 14.73), ('CA', 'LYS', 'OD2', 'ASP', 16.11), ('CA', 'LYS', 'O', 'ASP', 18.11), ('CA', 'LYS', 'C', 'ASP', 17.08), ('CA', 'LYS', 'CA', 'ASP', 16.93), ('CA', 'LYS', 'N', 'ASP', 15.85)],
        #                              [('N', 'LYS', 'CB', 'ASP', 17.32), ('N', 'LYS', 'CG', 'ASP', 16.18), ('N', 'LYS', 'OD1', 'ASP', 15.06), ('N', 'LYS', 'OD2', 'ASP', 16.5), ('N', 'LYS', 'O', 'ASP', 18.47), ('N', 'LYS', 'C', 'ASP', 17.38), ('N', 'LYS', 'CA', 'ASP', 17.12), ('N', 'LYS', 'N', 'ASP', 15.95)]]
        #
        # motif, total_pairs = fo.checkMatrixHelper(map=updated_map,pair=pair,motif=motif,filename=filename,totPairs=total_pairs)
        #
        # print "===========>  TEST 1 - Normal Matrix - from A_1a50_4_2_1_20 (his,lys,lys,asp) <============="
        # print motif


        # TEST 2: Double matrix with 2 same structures - from A_1a50_4_2_1_20 (his,lys,lys,asp)

        # motif = ""
        # filename = 'A_1a50_4_2_1_20'
        # total_pairs = []
        # pair = 'ASP_LYS'
        # updated_map = {}
        #
        # updated_map['distances'] = [[15.95, 14.57, 13.58, 12.13, 11.76, 18.62, 18.32, 17.07, 17.32],
        #                             [14.68, 13.35, 12.28, 10.86, 10.61, 17.33, 17.05, 15.85, 16.18],
        #                             [13.61, 12.25, 11.25, 9.79, 9.54, 16.23, 15.96, 14.73, 15.06],
        #                             [14.86, 13.6, 12.42, 11.08, 10.93, 17.49, 17.24, 16.11, 16.5],
        #                             [17.13, 15.75, 14.9, 13.41, 13.22, 19.49, 19.34, 18.11, 18.47],
        #                             [16.13, 14.71, 13.91, 12.4, 12.14, 18.54, 18.35, 17.08, 17.38],
        #                             [15.93, 14.5, 13.66, 12.15, 11.72, 18.54, 18.24, 16.93, 17.12],
        #                             [14.9, 13.43, 12.68, 11.17, 10.6, 17.58, 17.21, 15.85, 15.95],
        #                             [10.5, 11.12, 11.72, 12.51, 13.61, 12.59, 11.61, 10.32, 9.15],
        #                             [10.58, 11.31, 12.11, 12.99, 13.96, 12.25, 11.33, 10.12, 8.9],
        #                             [11.02, 11.91, 12.72, 13.72, 14.68, 12.54, 11.73, 10.5, 9.38],
        #                             [10.46, 11.1, 12.02, 12.81, 13.68, 11.89, 10.94, 9.88, 8.54],
        #                             [8.55, 9.33, 9.67, 10.67, 11.89, 11.09, 10.21, 8.73, 7.96],
        #                             [9.56, 10.43, 10.84, 11.88, 13.07, 11.88, 11.06, 9.59, 8.77],
        #                             [10.75, 11.49, 11.93, 12.83, 14.03, 13.02, 12.12, 10.71, 9.72],
        #                             [11.99, 12.82, 13.3, 14.25, 15.42, 14.09, 13.25, 11.85, 10.86]]
        #
        # updated_map['comparisons'] = [[('CB', 'ASP', 'CB', 'LYS', 15.95),  ('CB', 'ASP', 'CG', 'LYS', 14.57),  ('CB', 'ASP', 'CD', 'LYS', 13.58), ('CB', 'ASP', 'CE', 'LYS', 12.13), ('CB', 'ASP', 'NZ', 'LYS', 11.76), ('CB', 'ASP', 'O', 'LYS', 18.62), ('CB', 'ASP', 'C', 'LYS', 18.32), ('CB', 'ASP', 'CA', 'LYS', 17.07), ('CB', 'ASP', 'N', 'LYS', 17.32)],
        #                              [('CG', 'ASP', 'CB', 'LYS', 14.68),  ('CG', 'ASP', 'CG', 'LYS', 13.35),  ('CG', 'ASP', 'CD', 'LYS', 12.28), ('CG', 'ASP', 'CE', 'LYS', 10.86), ('CG', 'ASP', 'NZ', 'LYS', 10.61), ('CG', 'ASP', 'O', 'LYS', 17.33), ('CG', 'ASP', 'C', 'LYS', 17.05), ('CG', 'ASP', 'CA', 'LYS', 15.85), ('CG', 'ASP', 'N', 'LYS', 16.18)],
        #                              [('OD1', 'ASP', 'CB', 'LYS', 13.61), ('OD1', 'ASP', 'CG', 'LYS', 12.25), ('OD1', 'ASP', 'CD', 'LYS', 11.25), ('OD1', 'ASP', 'CE', 'LYS', 9.79), ('OD1', 'ASP', 'NZ', 'LYS', 9.54), ('OD1', 'ASP', 'O', 'LYS', 16.23), ('OD1', 'ASP', 'C', 'LYS', 15.96), ('OD1', 'ASP', 'CA', 'LYS', 14.73), ('OD1', 'ASP', 'N', 'LYS', 15.06)],
        #                              [('OD2', 'ASP', 'CB', 'LYS', 14.86), ('OD2', 'ASP', 'CG', 'LYS', 13.6),  ('OD2', 'ASP', 'CD', 'LYS', 12.42), ('OD2', 'ASP', 'CE', 'LYS', 11.08), ('OD2', 'ASP', 'NZ', 'LYS', 10.93), ('OD2', 'ASP', 'O', 'LYS', 17.49), ('OD2', 'ASP', 'C', 'LYS', 17.24), ('OD2', 'ASP', 'CA', 'LYS', 16.11), ('OD2', 'ASP', 'N', 'LYS', 16.5)],
        #                              [('O', 'ASP', 'CB', 'LYS', 17.13),   ('O', 'ASP', 'CG', 'LYS', 15.75),   ('O', 'ASP', 'CD', 'LYS', 14.9), ('O', 'ASP', 'CE', 'LYS', 13.41), ('O', 'ASP', 'NZ', 'LYS', 13.22), ('O', 'ASP', 'O', 'LYS', 19.49), ('O', 'ASP', 'C', 'LYS', 19.34), ('O', 'ASP', 'CA', 'LYS', 18.11), ('O', 'ASP', 'N', 'LYS', 18.47)],
        #                              [('C', 'ASP', 'CB', 'LYS', 16.13),   ('C', 'ASP', 'CG', 'LYS', 14.71),   ('C', 'ASP', 'CD', 'LYS', 13.91), ('C', 'ASP', 'CE', 'LYS', 12.4), ('C', 'ASP', 'NZ', 'LYS', 12.14), ('C', 'ASP', 'O', 'LYS', 18.54), ('C', 'ASP', 'C', 'LYS', 18.35), ('C', 'ASP', 'CA', 'LYS', 17.08), ('C', 'ASP', 'N', 'LYS', 17.38)],
        #                              [('CA', 'ASP', 'CB', 'LYS', 15.93),  ('CA', 'ASP', 'CG', 'LYS', 14.5),   ('CA', 'ASP', 'CD', 'LYS', 13.66), ('CA', 'ASP', 'CE', 'LYS', 12.15), ('CA', 'ASP', 'NZ', 'LYS', 11.72), ('CA', 'ASP', 'O', 'LYS', 18.54), ('CA', 'ASP', 'C', 'LYS', 18.24), ('CA', 'ASP', 'CA', 'LYS', 16.93), ('CA', 'ASP', 'N', 'LYS', 17.12)],
        #                              [('N', 'ASP', 'CB', 'LYS', 14.9),    ('N', 'ASP', 'CG', 'LYS', 13.43),   ('N', 'ASP', 'CD', 'LYS', 12.68), ('N', 'ASP', 'CE', 'LYS', 11.17), ('N', 'ASP', 'NZ', 'LYS', 10.6), ('N', 'ASP', 'O', 'LYS', 17.58), ('N', 'ASP', 'C', 'LYS', 17.21), ('N', 'ASP', 'CA', 'LYS', 15.85), ('N', 'ASP', 'N', 'LYS', 15.95)],
        #                              [('CB', 'ASP', 'CB', 'LYS', 10.5),   ('CB', 'ASP', 'CG', 'LYS', 11.12),  ('CB', 'ASP', 'CD', 'LYS', 11.72), ('CB', 'ASP', 'CE', 'LYS', 12.51), ('CB', 'ASP', 'NZ', 'LYS', 13.61), ('CB', 'ASP', 'O', 'LYS', 12.59), ('CB', 'ASP', 'C', 'LYS', 11.61), ('CB', 'ASP', 'CA', 'LYS', 10.32), ('CB', 'ASP', 'N', 'LYS', 9.15)],
        #                              [('CG', 'ASP', 'CB', 'LYS', 10.58),  ('CG', 'ASP', 'CG', 'LYS', 11.31),  ('CG', 'ASP', 'CD', 'LYS', 12.11), ('CG', 'ASP', 'CE', 'LYS', 12.99), ('CG', 'ASP', 'NZ', 'LYS', 13.96), ('CG', 'ASP', 'O', 'LYS', 12.25), ('CG', 'ASP', 'C', 'LYS', 11.33), ('CG', 'ASP', 'CA', 'LYS', 10.12), ('CG', 'ASP', 'N', 'LYS', 8.9)],
        #                              [('OD1', 'ASP', 'CB', 'LYS', 11.02), ('OD1', 'ASP', 'CG', 'LYS', 11.91), ('OD1', 'ASP', 'CD', 'LYS', 12.72), ('OD1', 'ASP', 'CE', 'LYS', 13.72), ('OD1', 'ASP', 'NZ', 'LYS', 14.68), ('OD1', 'ASP', 'O', 'LYS', 12.54), ('OD1', 'ASP', 'C', 'LYS', 11.73), ('OD1', 'ASP', 'CA', 'LYS', 10.5), ('OD1', 'ASP', 'N', 'LYS', 9.38)],
        #                              [('OD2', 'ASP', 'CB', 'LYS', 10.46), ('OD2', 'ASP', 'CG', 'LYS', 11.1),  ('OD2', 'ASP', 'CD', 'LYS', 12.02), ('OD2', 'ASP', 'CE', 'LYS', 12.81), ('OD2', 'ASP', 'NZ', 'LYS', 13.68), ('OD2', 'ASP', 'O', 'LYS', 11.89), ('OD2', 'ASP', 'C', 'LYS', 10.94), ('OD2', 'ASP', 'CA', 'LYS', 9.88), ('OD2', 'ASP', 'N', 'LYS', 8.54)],
        #                              [('O', 'ASP', 'CB', 'LYS', 8.55),    ('O', 'ASP', 'CG', 'LYS', 9.33),    ('O', 'ASP', 'CD', 'LYS', 9.67), ('O', 'ASP', 'CE', 'LYS', 10.67), ('O', 'ASP', 'NZ', 'LYS', 11.89), ('O', 'ASP', 'O', 'LYS', 11.09), ('O', 'ASP', 'C', 'LYS', 10.21), ('O', 'ASP', 'CA', 'LYS', 8.73), ('O', 'ASP', 'N', 'LYS', 7.96)],
        #                              [('C', 'ASP', 'CB', 'LYS', 9.56),    ('C', 'ASP', 'CG', 'LYS', 10.43),   ('C', 'ASP', 'CD', 'LYS', 10.84), ('C', 'ASP', 'CE', 'LYS', 11.88), ('C', 'ASP', 'NZ', 'LYS', 13.07), ('C', 'ASP', 'O', 'LYS', 11.88), ('C', 'ASP', 'C', 'LYS', 11.06), ('C', 'ASP', 'CA', 'LYS', 9.59), ('C', 'ASP', 'N', 'LYS', 8.77)],
        #                              [('CA', 'ASP', 'CB', 'LYS', 10.75),  ('CA', 'ASP', 'CG', 'LYS', 11.49),  ('CA', 'ASP', 'CD', 'LYS', 11.93), ('CA', 'ASP', 'CE', 'LYS', 12.83), ('CA', 'ASP', 'NZ', 'LYS', 14.03), ('CA', 'ASP', 'O', 'LYS', 13.02), ('CA', 'ASP', 'C', 'LYS', 12.12), ('CA', 'ASP', 'CA', 'LYS', 10.71), ('CA', 'ASP', 'N', 'LYS', 9.72)],
        #                              [('N', 'ASP', 'CB', 'LYS', 11.99),   ('N', 'ASP', 'CG', 'LYS', 12.82),   ('N', 'ASP', 'CD', 'LYS', 13.3), ('N', 'ASP', 'CE', 'LYS', 14.25), ('N', 'ASP', 'NZ', 'LYS', 15.42), ('N', 'ASP', 'O', 'LYS', 14.09), ('N', 'ASP', 'C', 'LYS', 13.25), ('N', 'ASP', 'CA', 'LYS', 11.85), ('N', 'ASP', 'N', 'LYS', 10.86)]]
        #
        # motif, total_pairs = fo.checkMatrixHelper(map=updated_map, pair=pair, motif=motif, filename=filename, \
        #                                           totPairs=total_pairs)
        # print "===========>  TEST 2 - Double matrix with 2 same structures - from A_1a50_4_2_1_20 (his,lys,lys,asp) <============="
        # print motif


        # TEST 3: 2 Structures with different sizes - from A_1a65_1_10_3_2 (his,cys,his)

        # motif = ""
        # filename = 'A_1a65_1_10_3_2'
        # total_pairs = []
        # pair = 'CYS_HIS'
        # updated_map = {}
        #
        # updated_map['distances'] = [[7.27, 7.81, 7.42, 9.1, 8.53, 9.44],
        #                             [8.86, 9.15, 8.5, 10.36, 9.41, 10.47],
        #                             [6.02, 5.79, 4.84, 6.95, 5.73, 6.88],
        #                             [6.41, 6.3, 5.51, 7.4, 6.36, 7.4],
        #                             [6.29, 6.65, 6.28, 7.84, 7.33, 8.16],
        #                             [5.02, 5.68, 5.72, 6.92, 6.91, 7.52],
        #                             [7.77, 9.03, 9.76, 9.9, 10.91, 11.0, 8.19, 7.0, 6.6, 5.33],
        #                             [7.4, 8.77, 9.36, 9.84, 10.64, 10.9, 7.48, 6.31, 6.32, 5.23],
        #                             [6.04, 6.84, 7.41, 7.6, 8.37, 8.49, 6.3, 5.38, 4.7, 4.25],
        #                             [5.58, 6.67, 7.46, 7.47, 8.52, 8.54, 6.4, 5.29, 4.4, 3.34],
        #                             [6.78, 7.99, 8.89, 8.68, 9.94, 9.85, 7.81, 6.63, 5.79, 4.44],
        #                             [7.61, 8.63, 9.57, 9.11, 10.48, 10.24, 8.78, 7.69, 6.69, 5.51]]
        #
        # updated_map['comparisons'] = [[('CB', 'CYS', 'CB', 'HIS', 7.27), ('CB', 'CYS', 'CG', 'HIS', 7.81), ('CB', 'CYS', 'ND1', 'HIS', 7.42), ('CB', 'CYS', 'CD2', 'HIS', 9.1), ('CB', 'CYS', 'CE1', 'HIS', 8.53), ('CB', 'CYS', 'NE2', 'HIS', 9.44)],
        #                              [('SG', 'CYS', 'CB', 'HIS', 8.86), ('SG', 'CYS', 'CG', 'HIS', 9.15), ('SG', 'CYS', 'ND1', 'HIS', 8.5), ('SG', 'CYS', 'CD2', 'HIS', 10.36), ('SG', 'CYS', 'CE1', 'HIS', 9.41), ('SG', 'CYS', 'NE2', 'HIS', 10.47)],
        #                              [('O', 'CYS', 'CB', 'HIS', 6.02), ('O', 'CYS', 'CG', 'HIS', 5.79), ('O', 'CYS', 'ND1', 'HIS', 4.84), ('O', 'CYS', 'CD2', 'HIS', 6.95), ('O', 'CYS', 'CE1', 'HIS', 5.73), ('O', 'CYS', 'NE2', 'HIS', 6.88)],
        #                              [('C', 'CYS', 'CB', 'HIS', 6.41), ('C', 'CYS', 'CG', 'HIS', 6.3), ('C', 'CYS', 'ND1', 'HIS', 5.51), ('C', 'CYS', 'CD2', 'HIS', 7.4), ('C', 'CYS', 'CE1', 'HIS', 6.36), ('C', 'CYS', 'NE2', 'HIS', 7.4)],
        #                              [('CA', 'CYS', 'CB', 'HIS', 6.29), ('CA', 'CYS', 'CG', 'HIS', 6.65), ('CA', 'CYS', 'ND1', 'HIS', 6.28), ('CA', 'CYS', 'CD2', 'HIS', 7.84), ('CA', 'CYS', 'CE1', 'HIS', 7.33), ('CA', 'CYS', 'NE2', 'HIS', 8.16)],
        #                              [('N', 'CYS', 'CB', 'HIS', 5.02), ('N', 'CYS', 'CG', 'HIS', 5.68), ('N', 'CYS', 'ND1', 'HIS', 5.72), ('N', 'CYS', 'CD2', 'HIS', 6.92), ('N', 'CYS', 'CE1', 'HIS', 6.91), ('N', 'CYS', 'NE2', 'HIS', 7.52)],
        #                              [('CB', 'CYS', 'CB', 'HIS', 7.77), ('CB', 'CYS', 'CG', 'HIS', 9.03), ('CB', 'CYS', 'ND1', 'HIS', 9.76), ('CB', 'CYS', 'CD2', 'HIS', 9.9), ('CB', 'CYS', 'CE1', 'HIS', 10.91), ('CB', 'CYS', 'NE2', 'HIS', 11.0), ('CB', 'CYS', 'O', 'HIS', 8.19), ('CB', 'CYS', 'C', 'HIS', 7.0), ('CB', 'CYS', 'CA', 'HIS', 6.6), ('CB', 'CYS', 'N', 'HIS', 5.33)],
        #                              [('SG', 'CYS', 'CB', 'HIS', 7.4), ('SG', 'CYS', 'CG', 'HIS', 8.77), ('SG', 'CYS', 'ND1', 'HIS', 9.36), ('SG', 'CYS', 'CD2', 'HIS', 9.84), ('SG', 'CYS', 'CE1', 'HIS', 10.64), ('SG', 'CYS', 'NE2', 'HIS', 10.9), ('SG', 'CYS', 'O', 'HIS', 7.48), ('SG', 'CYS', 'C', 'HIS', 6.31), ('SG', 'CYS', 'CA', 'HIS', 6.32), ('SG', 'CYS', 'N', 'HIS', 5.23)],
        #                              [('O', 'CYS', 'CB', 'HIS', 6.04), ('O', 'CYS', 'CG', 'HIS', 6.84), ('O', 'CYS', 'ND1', 'HIS', 7.41), ('O', 'CYS', 'CD2', 'HIS', 7.6), ('O', 'CYS', 'CE1', 'HIS', 8.37), ('O', 'CYS', 'NE2', 'HIS', 8.49), ('O', 'CYS', 'O', 'HIS', 6.3), ('O', 'CYS', 'C', 'HIS', 5.38), ('O', 'CYS', 'CA', 'HIS', 4.7), ('O', 'CYS', 'N', 'HIS', 4.25)],
        #                              [('C', 'CYS', 'CB', 'HIS', 5.58), ('C', 'CYS', 'CG', 'HIS', 6.67), ('C', 'CYS', 'ND1', 'HIS', 7.46), ('C', 'CYS', 'CD2', 'HIS', 7.47), ('C', 'CYS', 'CE1', 'HIS', 8.52), ('C', 'CYS', 'NE2', 'HIS', 8.54), ('C', 'CYS', 'O', 'HIS', 6.4), ('C', 'CYS', 'C', 'HIS', 5.29), ('C', 'CYS', 'CA', 'HIS', 4.4), ('C', 'CYS', 'N', 'HIS', 3.34)],
        #                              [('CA', 'CYS', 'CB', 'HIS', 6.78), ('CA', 'CYS', 'CG', 'HIS', 7.99), ('CA', 'CYS', 'ND1', 'HIS', 8.89), ('CA', 'CYS', 'CD2', 'HIS', 8.68), ('CA', 'CYS', 'CE1', 'HIS', 9.94), ('CA', 'CYS', 'NE2', 'HIS', 9.85), ('CA', 'CYS', 'O', 'HIS', 7.81), ('CA', 'CYS', 'C', 'HIS', 6.63), ('CA', 'CYS', 'CA', 'HIS', 5.79), ('CA', 'CYS', 'N', 'HIS', 4.44)],
        #                              [('N', 'CYS', 'CB', 'HIS', 7.61), ('N', 'CYS', 'CG', 'HIS', 8.63), ('N', 'CYS', 'ND1', 'HIS', 9.57), ('N', 'CYS', 'CD2', 'HIS', 9.11), ('N', 'CYS', 'CE1', 'HIS', 10.48), ('N', 'CYS', 'NE2', 'HIS', 10.24), ('N', 'CYS', 'O', 'HIS', 8.78), ('N', 'CYS', 'C', 'HIS', 7.69), ('N', 'CYS', 'CA', 'HIS', 6.69), ('N', 'CYS', 'N', 'HIS', 5.51)]]
        #
        # motif, total_pairs = fo.checkMatrixHelper(map=updated_map, pair=pair, motif=motif, filename=filename, \
        #                                           totPairs=total_pairs)
        #
        # print "===========>  TEST 3 - 2 Structures with different sizes - from A_1a65_1_10_3_2 (his,cys,his) <============="
        # print motif


        # TEST 4: 2 structures - different in atom 2 - from A_1cwy_2_4_1_25 (asp,glu,asp) *** MODIFIED FOR TESTING ***

        # motif = ""
        # filename = 'A_1cwy_2_4_1_25'
        # total_pairs = []
        # pair = 'GLU_ASP'
        # updated_map = {}
        #
        # updated_map['distances']   = [[6.55,  6.53,  7.5,   5.91,  6.94,  5.88],
        #                               [6.72,  6.23,  7.05,  5.4,   7.6,   6.42],
        #                               [7.05,  6.42,  6.93,  5.82,  7.52,  6.36],
        #                               [6.34,  5.71,  6.06,  5.41,  6.61,  5.49],
        #                               [8.29,  7.58,  8.0,   6.95,  8.6,   7.49],
        #                               [8.23,  8.27,  8.92,  8.0,   7.23,  6.48],
        #                               [8.62,  8.59,  9.35,  8.11,  8.06,  7.21],
        #                               [7.99,  8.04,  8.98,  7.43,  7.92,  7.0],
        #                               [8.31,  8.67,  9.67,  8.21,  7.82,  7.12],
        #                               [11.9,  11.43, 12.33, 10.3,  14.62, 13.93, 13.0,  12.58],
        #                               [10.53, 10.14, 11.1,  9.01,  13.19, 12.55, 11.67, 11.35],
        #                               [10.62, 10.24, 11.24, 9.07,  13.2,  12.7,  11.91, 11.8],
        #                               [10.82, 10.27, 11.19, 9.06,  13.48, 13.04, 12.18, 12.16],
        #                               [10.75, 10.56, 11.64, 9.45,  13.13, 12.69, 12.05, 12.01],
        #                               [13.74, 13.35, 14.32, 12.17, 16.3,  15.77, 14.99, 14.78],
        #                               [13.41, 13.13, 14.14, 12.01, 15.92, 15.32, 14.59, 14.29],
        #                               [12.94, 12.61, 13.57, 11.52, 15.53, 14.83, 14.01, 13.56],
        #                               [14.22, 13.83, 14.73, 12.73, 16.87, 16.13, 15.26, 14.74]]
        #
        # updated_map['comparisons'] = [[('CB', 'GLU', 'CB', 'ASP', 6.55), ('CB', 'GLU', 'CG', 'ASP', 6.53), ('CB', 'GLU', 'OD1', 'ASP', 7.5), ('CB', 'GLU', 'OD2', 'ASP', 5.91), ('CB', 'GLU', 'O', 'ASP', 6.94), ('CB', 'GLU', 'C', 'ASP', 5.88)],
        #                              [('CG', 'GLU', 'CB', 'ASP', 6.72), ('CG', 'GLU', 'CG', 'ASP', 6.23), ('CG', 'GLU', 'OD1', 'ASP', 7.05), ('CG', 'GLU', 'OD2', 'ASP', 5.4), ('CG', 'GLU', 'O', 'ASP', 7.6), ('CG', 'GLU', 'C', 'ASP', 6.42)],
        #                              [('CD', 'GLU', 'CB', 'ASP', 7.05), ('CD', 'GLU', 'CG', 'ASP', 6.42), ('CD', 'GLU', 'OD1', 'ASP', 6.93), ('CD', 'GLU', 'OD2', 'ASP', 5.82), ('CD', 'GLU', 'O', 'ASP', 7.52), ('CD', 'GLU', 'C', 'ASP', 6.36)],
        #                              [('OE1', 'GLU', 'CB', 'ASP', 6.34), ('OE1', 'GLU', 'CG', 'ASP', 5.71), ('OE1', 'GLU', 'OD1', 'ASP', 6.06), ('OE1', 'GLU', 'OD2', 'ASP', 5.41), ('OE1', 'GLU', 'O', 'ASP', 6.61), ('OE1', 'GLU', 'C', 'ASP', 5.49)],
        #                              [('OE2', 'GLU', 'CB', 'ASP', 8.29), ('OE2', 'GLU', 'CG', 'ASP', 7.58), ('OE2', 'GLU', 'OD1', 'ASP', 8.0), ('OE2', 'GLU', 'OD2', 'ASP', 6.95), ('OE2', 'GLU', 'O', 'ASP', 8.6), ('OE2', 'GLU', 'C', 'ASP', 7.49)],
        #                              [('O', 'GLU', 'CB', 'ASP', 8.23), ('O', 'GLU', 'CG', 'ASP', 8.27), ('O', 'GLU', 'OD1', 'ASP', 8.92), ('O', 'GLU', 'OD2', 'ASP', 8.0), ('O', 'GLU', 'O', 'ASP', 7.23), ('O', 'GLU', 'C', 'ASP', 6.48)],
        #                              [('C', 'GLU', 'CB', 'ASP', 8.62), ('C', 'GLU', 'CG', 'ASP', 8.59), ('C', 'GLU', 'OD1', 'ASP', 9.35), ('C', 'GLU', 'OD2', 'ASP', 8.11), ('C', 'GLU', 'O', 'ASP', 8.06), ('C', 'GLU', 'C', 'ASP', 7.21)],
        #                              [('CA', 'GLU', 'CB', 'ASP', 7.99), ('CA', 'GLU', 'CG', 'ASP', 8.04), ('CA', 'GLU', 'OD1', 'ASP', 8.98), ('CA', 'GLU', 'OD2', 'ASP', 7.43), ('CA', 'GLU', 'O', 'ASP', 7.92), ('CA', 'GLU', 'C', 'ASP', 7.0)],
        #                              [('N', 'GLU', 'CB', 'ASP', 8.31), ('N', 'GLU', 'CG', 'ASP', 8.67), ('N', 'GLU', 'OD1', 'ASP', 9.67), ('N', 'GLU', 'OD2', 'ASP', 8.21), ('N', 'GLU', 'O', 'ASP', 7.82), ('N', 'GLU', 'C', 'ASP', 7.12)],
        #                              [('CB', 'GLU', 'CB', 'ASP', 11.9), ('CB', 'GLU', 'CG', 'ASP', 11.43), ('CB', 'GLU', 'OD1', 'ASP', 12.33), ('CB', 'GLU', 'OD2', 'ASP', 10.3), ('CB', 'GLU', 'O', 'ASP', 14.62), ('CB', 'GLU', 'C', 'ASP', 13.93), ('CB', 'GLU', 'CA', 'ASP', 13.0), ('CB', 'GLU', 'N', 'ASP', 12.58)],
        #                              [('CG', 'GLU', 'CB', 'ASP', 10.53), ('CG', 'GLU', 'CG', 'ASP', 10.14), ('CG', 'GLU', 'OD1', 'ASP', 11.1), ('CG', 'GLU', 'OD2', 'ASP', 9.01), ('CG', 'GLU', 'O', 'ASP', 13.19), ('CG', 'GLU', 'C', 'ASP', 12.55), ('CG', 'GLU', 'CA', 'ASP', 11.67), ('CG', 'GLU', 'N', 'ASP', 11.35)],
        #                              [('CD', 'GLU', 'CB', 'ASP', 10.62), ('CD', 'GLU', 'CG', 'ASP', 10.24), ('CD', 'GLU', 'OD1', 'ASP', 11.24), ('CD', 'GLU', 'OD2', 'ASP', 9.07), ('CD', 'GLU', 'O', 'ASP', 13.2), ('CD', 'GLU', 'C', 'ASP', 12.7), ('CD', 'GLU', 'CA', 'ASP', 11.91), ('CD', 'GLU', 'N', 'ASP', 11.8)],
        #                              [('OE1', 'GLU', 'CB', 'ASP', 10.82), ('OE1', 'GLU', 'CG', 'ASP', 10.27), ('OE1', 'GLU', 'OD1', 'ASP', 11.19), ('OE1', 'GLU', 'OD2', 'ASP', 9.06), ('OE1', 'GLU', 'O', 'ASP', 13.48), ('OE1', 'GLU', 'C', 'ASP', 13.04), ('OE1', 'GLU', 'CA', 'ASP', 12.18), ('OE1', 'GLU', 'N', 'ASP', 12.16)],
        #                              [('OE2', 'GLU', 'CB', 'ASP', 10.75), ('OE2', 'GLU', 'CG', 'ASP', 10.56), ('OE2', 'GLU', 'OD1', 'ASP', 11.64), ('OE2', 'GLU', 'OD2', 'ASP', 9.45), ('OE2', 'GLU', 'O', 'ASP', 13.13), ('OE2', 'GLU', 'C', 'ASP', 12.69), ('OE2', 'GLU', 'CA', 'ASP', 12.05), ('OE2', 'GLU', 'N', 'ASP', 12.01)],
        #                              [('O', 'GLU', 'CB', 'ASP', 13.74), ('O', 'GLU', 'CG', 'ASP', 13.35), ('O', 'GLU', 'OD1', 'ASP', 14.32), ('O', 'GLU', 'OD2', 'ASP', 12.17), ('O', 'GLU', 'O', 'ASP', 16.3), ('O', 'GLU', 'C', 'ASP', 15.77), ('O', 'GLU', 'CA', 'ASP', 14.99), ('O', 'GLU', 'N', 'ASP', 14.78)],
        #                              [('C', 'GLU', 'CB', 'ASP', 13.41), ('C', 'GLU', 'CG', 'ASP', 13.13), ('C', 'GLU', 'OD1', 'ASP', 14.14), ('C', 'GLU', 'OD2', 'ASP', 12.01), ('C', 'GLU', 'O', 'ASP', 15.92), ('C', 'GLU', 'C', 'ASP', 15.32), ('C', 'GLU', 'CA', 'ASP', 14.59), ('C', 'GLU', 'N', 'ASP', 14.29)],
        #                              [('CA', 'GLU', 'CB', 'ASP', 12.94), ('CA', 'GLU', 'CG', 'ASP', 12.61), ('CA', 'GLU', 'OD1', 'ASP', 13.57), ('CA', 'GLU', 'OD2', 'ASP', 11.52), ('CA', 'GLU', 'O', 'ASP', 15.53), ('CA', 'GLU', 'C', 'ASP', 14.83), ('CA', 'GLU', 'CA', 'ASP', 14.01), ('CA', 'GLU', 'N', 'ASP', 13.56)],
        #                              [('N', 'GLU', 'CB', 'ASP', 14.22), ('N', 'GLU', 'CG', 'ASP', 13.83), ('N', 'GLU', 'OD1', 'ASP', 14.73), ('N', 'GLU', 'OD2', 'ASP', 12.73), ('N', 'GLU', 'O', 'ASP', 16.87), ('N', 'GLU', 'C', 'ASP', 16.13), ('N', 'GLU', 'CA', 'ASP', 15.26), ('N', 'GLU', 'N', 'ASP', 14.74)]]
        #
        # motif, total_pairs = fo.checkMatrixHelper(map=updated_map, pair=pair, motif=motif, filename=filename, \
        #                                           totPairs=total_pairs)
        #
        # print "=============>  TEST 4 - 2 structures - different in atom 2 - from A_1cwy_2_4_1_25 (asp,glu,asp) *** MODIFIED FOR TESTING ***<============="
        # print motif


        # TEST 5: Three Structures - M_1ah7_3_1_4_3 (asp,zn,zn,zn)
        # motif = ""
        # filename = 'M_1ah7_3_1_4_3'
        # total_pairs = []
        # pair = 'ASP_ZN'
        # updated_map = {}
        #
        #
        # updated_map['distances']   = [[6.65],
        #                               [5.3],
        #                               [4.29],
        #                               [5.57],
        #                               [10.33],
        #                               [9.03],
        #                               [8.83],
        #                               [8.37],
        #                               [8.45],
        #                               [7.02],
        #                               [6.83],
        #                               [6.25]]
        # updated_map['comparisons'] = [[('CB', 'ASP', 'ZN', 'ZN', 6.65)],
        #                              [('CG', 'ASP', 'ZN', 'ZN', 5.3)],
        #                              [('OD1', 'ASP', 'ZN', 'ZN', 4.29)],
        #                              [('OD2', 'ASP', 'ZN', 'ZN', 5.57)],
        #                              [('CB', 'ASP', 'ZN', 'ZN', 10.33)],
        #                              [('CG', 'ASP', 'ZN', 'ZN', 9.03)],
        #                              [('OD1', 'ASP', 'ZN', 'ZN', 8.83)],
        #                              [('OD2', 'ASP', 'ZN', 'ZN', 8.37)],
        #                              [('CB', 'ASP', 'ZN', 'ZN', 8.45)],
        #                              [('CG', 'ASP', 'ZN', 'ZN', 7.02)],
        #                              [('OD1', 'ASP', 'ZN', 'ZN', 6.83)],
        #                              [('OD2', 'ASP', 'ZN', 'ZN', 6.25)]]
        #
        # motif, total_pairs = fo.checkMatrixHelper(map=updated_map, pair=pair, motif=motif, filename=filename, \
        #                                        totPairs=total_pairs)
        #
        # print "=============>  TEST 5: Three Structures - M_1ah7_3_1_4_3 (asp,zn,zn,zn)<============="
        #
        # print motif



if __name__ == '__main__':

    global d
    d = 1.0
    main()
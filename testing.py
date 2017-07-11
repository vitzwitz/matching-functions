from functions import *
from ParseOnlyAtoms import *
from Classes import *
# import kdtreeCOPY as kdc
import kdtrees4atoms as kdt
import time as t


def testDistBasedCluster():
    # For categorizing all points
    pdbID = raw_input("Enter a pdb code: ")
    path = urllib.urlretrieve('http://files.rcsb.org/download/%s.pdb' % pdbID,
                              'C:/Users/Brianna/Downloads/proteinDATA/%s.pdb' % pdbID)
    try:
        file = 'C:/Users/blm7643/Downloads/proteinDATA/%s.pdb' % pdbID
        pdbData = readFile(file)
    except IOError:
        file = '%s.pdb' % pdbID
        pdbData = readFile(file)

    Clusters = {}
    Atoms = pdbData["Atom"]
    ptr = Atoms[0]
    r = 0.5
    # K = 10
    print "Atoms:", len(Atoms)

    cluster, other, flag = createClusterbasedonDistance(r, ptr, Atoms)  # First Cluster
    Clusters[ptr, r] = cluster  # First cluster stored
    curr = other  # Temp other
    # while len(cluster) != len(Atoms):
    while curr != []:
        r += r  # New Class
        cluster, other, flag = createClusterbasedonDistance(r, ptr, curr)  # New Cluster
        Clusters[r] = cluster  # Store Cluster
        curr = other

def testBasicDistCluster():
    # For finding atoms within a distance of a point
    pdbID = raw_input("Enter a pdb code: ")
    path = urllib.urlretrieve('http://files.rcsb.org/download/%s.pdb' % pdbID,
                              'C:/Users/Brianna/Downloads/proteinDATA/%s.pdb' % pdbID)
    try:
        file = 'C:/Users/blm7643/Downloads/proteinDATA/%s.pdb' % pdbID
        pdbData = readFile(file)
    except IOError:
        file = '%s.pdb' % pdbID
        pdbData = readFile(file)

    Clusters = {}
    Atoms = pdbData["Atom"]
    ptr = Atoms[0]
    r = 0.5
    # K = 10        # Limit cluster size ? If
    print "Atoms:", len(Atoms)

    cluster, other, flag = createClusterbasedonDistance(r, ptr, Atoms)  # First Cluster
    Clusters[ptr, r] = cluster  # First cluster stored
    curr = other  # Temp other
    # while len(cluster) != len(Atoms):
    while curr != []:
        r += r  # New Class
        cluster, other, flag = createClusterbasedonDistance(r, ptr, curr)  # New Cluster
        Clusters[r] = cluster  # Store Cluster
        curr = other

def testKBasedCluster():
    # For Testing:
        pdbID = raw_input("Enter a pdb code: ")
        path = urllib.urlretrieve('http://files.rcsb.org/download/%s.pdb' % pdbID,
                                  'C:/Users/Brianna/Downloads/proteinDATA/%s.pdb' % pdbID)
        try:
            file = 'C:/Users/blm7643/Downloads/proteinDATA/%s.pdb' % pdbID
            pdbData = readFile(file)
        except IOError:
            file = '%s.pdb' % pdbID
            pdbData = readFile(file)

        Atoms = pdbData["Atom"]
        ptr = Atoms[0]
        K = 10
        nearestNeighbors = createClusterBasedonK(ptr, Atoms, K)

        for neighbor in nearestNeighbors:
            print neighbor.name

def testkNN_w_inDistance():
    # For Testing:
    pdbID = raw_input("Enter a pdb code: ")
    path = urllib.urlretrieve('http://files.rcsb.org/download/%s.pdb' % pdbID,
                              'C:/Users/Brianna/Downloads/proteinDATA/%s.pdb' % pdbID)
    try:
        file = 'C:/Users/blm7643/Downloads/proteinDATA/%s.pdb' % pdbID
        pdbData = readFile(file)
    except IOError:
        file = '%s.pdb' % pdbID
        pdbData = readFile(file)

    Atoms = pdbData["Atom"]
    ptr = Atoms[0]
    K = 10
    distance = 10
    nearestNeighbors = kNN_wDistance(ptr, Atoms, K, distance)


def testingKNN_specificAtoms():
    pdbID = raw_input("Enter a pdb code: ")
    path = urllib.urlretrieve('http://files.rcsb.org/download/%s.pdb' % pdbID,
                              'C:/Users/Brianna/Downloads/proteinDATA/%s.pdb' % pdbID)
    try:
        file = 'C:/Users/blm7643/Downloads/proteinDATA/%s.pdb' % pdbID
        pdbData = readFile(file)
    except IOError:
        file = '%s.pdb' % pdbID
        pdbData = readFile(file)

    Atoms = pdbData["Atom"]
    desiredAtoms = getSpecificAtom("CB", "GLU", Atoms)

    distance = 11.14
    constraint = ["SG", "CB", "CA", "C", "N", "O"]
    constraint.sort()
    K = len(constraint)

    for CB in desiredAtoms:
        neighbors, walking = kNN_resNames(Atoms, K, distance, CB, "CYS")
        if len(neighbors) == K:
            neighbors.sort()
            if neighbors == constraint:
                print CB.serial, CB.resSeq, ":", neighbors
                print walking

def testKDTrees():
        pdbID = raw_input("Enter a pdb code: ")
        path = urllib.urlretrieve('http://files.rcsb.org/download/%s.pdb' % pdbID,
                                  'C:/Users/Brianna/PycharmProjects/ClusterAlg/%s.pdb' % pdbID)
        try:
            file = 'C:/Users/blm7643/Downloads/proteinDATA/%s.pdb' % pdbID
            pdbData = readFile(file)
        except IOError:
            file = '%s.pdb' % pdbID
            pdbData = readFile(file)

        distance = 11.14
        constraint = ["SG", "CB", "CA", "C", "N", "O"]
        single = ["O", "ASN"]
        mult = [["O", "ASN"], ["SG", "ASN"]]
        Atoms = pdbData["Atom"]
        start = t.time()
        treee = kdt.KDTree4Atoms(np.asarray(Atoms))
        treeeeee = t.time() - start
        # desiredAtoms = getSpecificAtom("CB", "GLU", Atoms)


        # neighs = tree.query(desiredAtoms[0], k=3, res="CYS")
        # for ne in neighs:
        #     print ne.resName
        # neighs = tree.query(desiredAtoms[0], res="CYS", atomName="SG")
        # print("===================")
        # neighss = tree.query(desiredAtoms[0], res="ASN", atomName="SG")
        # print desiredAtoms[0].position
        # neighs1 = tree.query_ball_point(desiredAtoms[0], 9.0, eps=0, res="GLU")
        # print len(neighs1), "\n", neighs1
        # neighs2 = tree.query_ball_point(desiredAtoms[0], 9.0, eps=0, res="ALA")
        # print len(neighs2), "\n", neighs2
        startQuery = t.time()
        # cmd.select('cys5', 'n. CB&r. cys w. %s of n. OE2&r. glu'%(d*10.70))
        neighS = treee.query_pairs(r=10.70, res1="CYS", res2="GLU", atomName1="CB", atomName2="OE2")
        queryyy = t.time() - startQuery
        print neighS
        print len(neighS)

        print("Building Tree:", treeeeee, "seconds")
        print("Motifing:", queryyy, "seconds")

        # print("**********************************************************************************")
        # neighB = treee.query_pairs(r=20., res1="CYS", res2="GLU", atomName1="CB", atomName2="OE2")
        # print neighB
        # print len(neighB)

        # print len(neigh[0])
        #
        # print "*************************** START ********************************"
        # for pair in neigh:
        #     print "CYS & CB", Atoms[pair[0]].resName, Atoms[pair[0]].name, Atoms[pair[0]].position
        #     print "GLU & CB", Atoms[pair[1]].resName, Atoms[pair[1]].name, Atoms[pair[1]].position
        #     print "*************************** NEXT ********************************"
        # print "*************************** END ********************************"
testKDTrees()


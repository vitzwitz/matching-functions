import functions as f
import ParserOnlyAtoms as poa
import Classes as cl
# import kdtreeCOPY as kdc
import kdtree4atoms as kdt
import time as t
import numpy as np

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
        execfile("A_1a4s_1_2_1_8.py")

if __name__ == '__main__':

    global d
    d = 1.0
    print "Trial 1"
    main()
    print "Trial 2"
    main()
    print "Trial 3"
    main()
    print "end"

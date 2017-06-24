from functions import *
from ParserOnlyAtoms import *
from Classes import *

def grabStandardAtomsFromPDB(pdbData):
    return pdbData["Atom"]

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
    Atoms = grabStandardAtomsFromPDB(pdbData)
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
    Atoms = grabStandardAtomsFromPDB(pdbData)
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

        Atoms = grabStandardAtomsFromPDB(pdbData)
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

    Atoms = grabStandardAtomsFromPDB(pdbData)
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

    Atoms = grabStandardAtomsFromPDB(pdbData)
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

testingKNN_specificAtoms()



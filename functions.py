"""
functions : Functions for clustering
"""

import math as m

def euclideanDistance(pt1, pt2):
    """
    euclideanDistance : finds distance between two positions
    euclideanDistance : tuple of floats * tuple of floats -> float
    :param pt1: point 1
    :param pt2: point 2
    :return: distance between 2 3D points
    """
    return m.sqrt((pt1[0] - pt2[0])**2 + (pt1[1] - pt2[1])**2 + (pt1[2] - pt2[2])**2)

def createClusterbasedonDistance(r, ptr, Atoms, K=""):
    """
    createCluster : Creates a cluster of all the atoms within a certain distance of a certain point

    createCluster -> float * list of floats * list of objects* int
    :param r: radius of cluster (float)
    :param ptr: point being compared (tuple of floats)
    :param Atoms: list of Atom objects
    :param K: max cluster size
    :return: cluster, the other atoms left, boolean (hitting max before comparing all atoms)
    """
    cluster = []
    other = []
    i = 0
    for atom in Atoms:

        if euclideanDistance((atom.x, atom.y, atom.z), (ptr.x, ptr.y, ptr.z)) <= r: # Atom in range
            # data = [atom.res, atom.name]
            cluster.append(atom.name)
        else:
            other.append(atom) # Atom object not in range
        i += 1
        if len(cluster) == K and len(Atoms) - i != 1 and K != "":    # Max Cluster size
            other += Atoms[i:]
            return cluster, other, False
    return cluster, other, True

def createClusterBasedonK(observer, Atoms, K):
    """
    createClusterBasedonK : Find K nearest neighbors of observer
    createClusterBasedonK -> object * list of atom objects * int

    pre-condition : K <= total atoms

    :param observer: atom object that is compared
    :param Atoms: list of atom objects
    :param K: number of nearest neighbors desired
    :return: tuple of K atom objects closest to observer
    """
    neighbors = ()
    for atom in Atoms:
        dist = euclideanDistance((atom.x, atom.y, atom.z), (observer.x, observer.y, observer.z))
        if len(neighbors) < 2*K:
            neighbors += (dist, atom)
            neighbors = sorted(neighbors)
        else:
            if dist < neighbors[K-1]:
                neighbors = neighbors[:(K-1)] + neighbors[K:(len(neighbors)-1)] + [dist, atom]
                neighbors = sorted(neighbors)

    return neighbors[K:2*K]

def kNN_wDistance(observer, Atoms, K, distance):
    """
    createClusterBasedonDist_N_K : Find K nearest neighbors of observer within a certain distance
    createClusterBasedonDist_N_K -> object * list of atom objects * int
    :param observer: atom object that is compared
    :param Atoms: list of atom objects
    :param K: desired number of nearest neighbors
    :param distance:
    :return:
    """

    neighbors = []
    walking = []
    totDists = []
    for atom in Atoms:
        d = euclideanDistance((atom.x, atom.y, atom.z), (observer.x, observer.y, observer.z))
        totDists.append(d)
        if len(neighbors) < K and d <= distance:
            neighbors.append(atom)
            walking.append(d)
        elif len(neighbors) == K and d <= distance:
            max = d
            marker = K+1
            for PO in range(len(walking)):
                if max < walking[PO]:
                    marker = PO
                    max = walking[PO]
            if marker < K+1:
                neighbors[marker] = atom
                walking[marker] = d
    return neighbors
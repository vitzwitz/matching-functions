"""
functions : Functions for clustering
"""

import kdtrees4atoms as kdt
import Classes as cl
import numpy as np

def euclideanDistance(pt1, pt2):
    """
    euclideanDistance : finds distance between two positions
    euclideanDistance : tuple of floats * tuple of floats -> float
    :param pt1: point 1
    :param pt2: point 2
    :return: distance between 2 3D points or array of distances
    """
    if pt1 != pt2:
        return euclideanDistanceHelper(pt1, pt2)
    else:
        return ((pt1[0] - pt2[0])**2 + (pt1[1] - pt2[1])**2 + (pt1[2] - pt2[2])**2)**(1/2.)


def euclideanDistanceHelper(pt1, pt2):
    ds = []
    if len(pt1) == 1:
        return euclideanDistance(pt2, pt1)
    if isinstance(pt1[0], cl.Atom):
        for atom in pt1:
            ds.append(euclideanDistance(atom.position, pt2))
    else:
        for pt in pt1:
            ds.append(euclideanDistance(pt, pt2))
    return np.asarray(ds)

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

def getResidues(resname, Atoms):
    # For testing
    res = []
    for atom in Atoms:
        if atom.resName == resname:
           res.append(atom)
    return res

def getSpecificAtom(atomname, resname, Atoms):
    # For testing
    desiredAtoms = []
    for atom in Atoms:
        if atom.resName.strip() == resname:
            if atom.name.strip() == atomname:
                desiredAtoms.append(atom)
    return desiredAtoms

def kNN_resNames(Atoms, K, distance, observer, resname):

    neighbors = []
    walking = []

    for atom in Atoms:
            d = euclideanDistance((atom.x, atom.y, atom.z), (observer.x, observer.y, observer.z))


            if len(neighbors) < K and d <= distance and atom.resName.strip() == resname:
                neighbors.append(atom.name)
                walking.append(d)

            elif len(neighbors) == K and d <= distance and atom.resName.strip() == resname:
                max = d
                marker = K+1
                for PO in range(len(walking)):
                    if max < walking[PO]:
                        marker = PO
                        max = walking[PO]
                if marker < K+1:
                    neighbors[marker] = atom.name
                    walking[marker] = d
    neighbors = selectionSort(walking, neighbors)
    return neighbors, walking

def selectionSort(VALS, NEIGHS):
    """
    selectionSort sorts a list of integers by
    moving them from the sequence they originate in
    into a new sequence, where the smallest numbers
    are placed first, then the largest
    :param lst: a list of numbers
    :return: the sorted list
    """

    for mark in range(len(VALS) - 1):
        idx = findMinFrom(VALS, mark)
        swap(VALS, mark, idx)
        swap(NEIGHS, mark, idx)
    return NEIGHS


def findMinFrom(lst, mark):
    """
    findMinFrom finds the minimum value in list from an index (mark)
    :param lst: a list of numbers
    :param mark: index in the list
    :return: index of the smallest number
    """

    index = mark
    min = lst[mark]

    for num in range(mark, len(lst)):
        if min > lst[num]:
            min = lst[num]
            index = num
    return index

def swap(lst, i, j):
    """
    swap swaps elements in a list
    :param i: an index
    :param j: another index
    :param lst: a list of numbers
    :return: list with swapped elements
    """
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp
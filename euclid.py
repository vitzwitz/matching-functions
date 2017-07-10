import numpy as np
import Classes as cl
from ParseOnlyAtoms import *

class errorr:
    """
    Idea came from python docs page: https://docs.python.org/2/tutorial/errors.html
    """
    pass
class ArgumentError(errorr):
    def __repr__(self):
        return "ArgumentError: Incorrect type of arguments"

def euclideanDistance(pt1, pt2):
    """
    euclideanDistance : finds distance between two positions
    euclideanDistance : tuple of floats * tuple of floats -> float
    :param pt1: point 1
    :param pt2: point 2
    :return: distance between 2 3D points or array of distances
    """
    if not (isinstance(pt1, list) or isinstance(pt1, tuple)):
        "pt1 -> array, atom, other"
        try:
            "pt1 -> array"
            pt1 = pt1.ravel()
            if isinstance(pt1, cl.Atom):
                pt1 = pt1.position
                return euclideanDistance(pt1, pt2)
            else:
                pt1 = list(pt1)
                return euclideanDistance(pt1, pt2)
        except AttributeError:
            try:
                "pt1 -> atom"
                pt1 = pt1.position
                return euclideanDistance(pt1, pt2)
            except AttributeError:
                "pt1 -> other"
                return ArgumentError
    if not (isinstance(pt2, list) or isinstance(pt2, tuple)):
        "pt2 -> array, atom, other"
        try:
            "pt2 -> array"
            pt2 = pt2.ravel()
            if isinstance(pt2, cl.Atom):
                pt2 = pt2.position
                return euclideanDistance(pt1, pt2)
            else:
                pt2 = list(pt2)
                return euclideanDistance(pt1, pt2)
        except AttributeError:
            try:
                "pt2 -> atom"
                pt2 = pt2.position
                return euclideanDistance(pt1, pt2)
            except AttributeError:
                "pt2 -> other"
                return ArgumentError
    if (isinstance(pt1, int) or isinstance(pt1, float)) or (isinstance(pt2, int) or isinstance(pt2, float)):
        "pt1 -> int, float"
        "pt2 -> int, float (one or both)"
        raise ArgumentError
    elif (isinstance(pt1, list) or isinstance(pt1, tuple)) and (isinstance(pt2, list) or isinstance(pt2, tuple)):
        "pt1 -> list/tuple"
        "pt2 -> list/tuple"

        if (isinstance(pt1[0], int) or isinstance(pt1[0], float)):
            "pt1 -> list/tuple of floats, ints"
            "pt2 -> list/tuple of floats, ints, tuples, lists, atoms"
            if(isinstance(pt2[0], int) or isinstance(pt2[0], float)):
                "pt1 -> list/tuple of floats, ints"
                "pt2 -> list/tuple of floats, ints"
                return ((pt1[0] - pt2[0])**2 + (pt1[1] - pt2[1])**2 + (pt1[2] - pt2[2])**2)**(1/2.)
            else:
                "pt1 -> list/tuple of floats, ints"
                "pt2 -> list/tuple of lists, tuples, atoms, other"
                if isinstance(pt2[0], list) or isinstance(pt2[0], tuple) or isinstance(pt2[0], cl.Atom):
                    "pt1 -> list/tuple of floats, ints"
                    "pt2 -> list/tuple of lists, tuples, atoms"
                    return euclideanDistanceHelper(pt1, pt2)
                else:
                    "pt1 -> list/tuple of floats, ints"
                    "pt2 -> list/tuple of other"
                    raise ArgumentError
        elif (isinstance(pt2[0], int) or isinstance(pt2[0], float)):
            "pt1 -> list/tuple of tuples, lists, atoms, other"
            "pt2 -> list/tuple of floats, ints"
            if isinstance(pt1[0], list) or isinstance(pt1[0], tuple) or isinstance(pt1[0], cl.Atom):
                "pt1 -> list/tuple of lists, tuples, atoms"
                "pt2 -> list/tuple of floats, ints"
                return euclideanDistanceHelper(pt1, pt2)
            else:
                "pt1 -> list/tuple of other"
                "pt2 -> list/tuple of floats, ints"
                raise ArgumentError
        elif (isinstance(pt1[0], cl.Atom) and isinstance(pt2[0], cl.Atom)):
            if len(pt1) == 1 and len(pt2) == 1:
                return euclideanDistance(pt1[0].position, pt2[0].position)
            elif len(pt2) == 1 and len(pt1) > 1:
                return euclideanDistance(pt1, pt2[0].position)
            elif len(pt1) == 1 and len(pt2) > 1:
                return euclideanDistance(pt1[0].position, pt2)
            else:
                return ArgumentError
        else:
            return ArgumentError


def euclideanDistanceHelper(pt1, pt2):
    """
    :param pt1: list/tuple of lists, tuples, or atoms
    :param pt2: list/tuple of ints, or floats
    :return: list of distances
    """
    ds = []
    if (isinstance(pt2[0], float) or isinstance(pt2[0], int)) and (isinstance(pt1[0], float) or isinstance(pt1[0], int)):
        raise Warning
    elif (isinstance(pt1[0], float) or isinstance(pt1[0], int)):
        return euclideanDistance(pt2, pt1)
    else:
        if isinstance(pt1[0], list) or isinstance(pt1[0], tuple):
            for pnt in pt1:
                ds.append(euclideanDistance(pnt, pt2))
            return ds
        else:
            for atm in pt1:
                try:
                    atm = atm.ravel()
                except AttributeError:
                    pass
                ds.append(euclideanDistance(atm.position, pt2))
            return ds
def TestThis():
    pdbID = raw_input("Enter a pdb code: ")
    path = urllib.urlretrieve('http://files.rcsb.org/download/%s.pdb' % pdbID,
                              'C:/Users/Brianna/PycharmProjects/ClusterAlg/%s.pdb' % pdbID)
    try:
        file = 'C:/Users/blm7643/Downloads/proteinDATA/%s.pdb' % pdbID
        pdbData = readFile(file)
    except IOError:
        file = '%s.pdb' % pdbID
        pdbData = readFile(file)
    Atoms = pdbData["Atom"]

    # print("Test 1: 2 tuples")
    # print("Correct", ((Atoms[0].position[0]- Atoms[1].position[0])**2. + (Atoms[0].position[1]- Atoms[1].position[1])**2. + (Atoms[0].position[2]- Atoms[1].position[2])**2.)**(1/2.))
    # print(euclideanDistance(Atoms[0].position, Atoms[1].position))
    # print("Test 2: 2 atoms")
    # print("Correct", ((Atoms[0].position[0]- Atoms[1].position[0])**2. + (Atoms[0].position[1]- Atoms[1].position[1])**2. + (Atoms[0].position[2]- Atoms[1].position[2])**2.)**(1/2.))
    # print(euclideanDistance(Atoms[0], Atoms[1]))
    # print("Test 3: 1 tuple, 1 atom")
    # print("Correct", ((Atoms[0].position[0]- Atoms[1].position[0])**2. + (Atoms[0].position[1]- Atoms[1].position[1])**2. + (Atoms[0].position[2]- Atoms[1].position[2])**2.)**(1/2.))
    # print(euclideanDistance(Atoms[0].position, Atoms[1]))
    # print("Test 4: 1 atom, 1 tuple")
    # print("Correct", ((Atoms[0].position[0]- Atoms[1].position[0])**2. + (Atoms[0].position[1]- Atoms[1].position[1])**2. + (Atoms[0].position[2]- Atoms[1].position[2])**2.)**(1/2.))
    # print(euclideanDistance(Atoms[0], Atoms[1].position))
    # print("Test 5: 1 atom, 2 atoms")
    # print("Correct", ((Atoms[0].position[0]- Atoms[1].position[0])**2. + (Atoms[0].position[1]- Atoms[1].position[1])**2. + (Atoms[0].position[2]- Atoms[1].position[2])**2.)**(1/2.))
    # print("Correct", ((Atoms[0].position[0]- Atoms[2].position[0])**2. + (Atoms[0].position[1]- Atoms[2].position[1])**2. + (Atoms[0].position[2]- Atoms[2].position[2])**2.)**(1/2.))
    # print(euclideanDistance(Atoms[0], Atoms[1:3]))
    # print("Test 6: lots of atoms, lots of atoms")
    # print(euclideanDistance(Atoms[0:5], Atoms[5:10]))
TestThis()
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
def defyingDimensions(operation, a, b, reverse=False):
    oper = []
    if len(b) > 1:
        temp = a
        a = b
        b = temp
    if isinstance(b, cl.Atom) == False:
        b = np.asarray(b)
    try:
        if len(b) > 1 and len(a) != len(b):
            raise Warning
    except AttributeError:
        if not (isinstance(b, cl.Atom) or isinstance(a,cl.Atom)):
            raise Warning
    except TypeError:
        pass
    if isinstance(a[0], cl.Atom):
        if isinstance(b, float) or isinstance(b,int):
            b = np.asarray([b])
        for atom in a:
            if operation == "-":
                if reverse == False:
                    oper.append(list(b - np.asarray(atom.position)))
                else:
                    oper.append(list(np.asarray(atom.position) - b))

            elif operation == "+":
                oper.append(tuple(b - np.asarray(atom.position)))

        return np.array(oper)
    elif isinstance(b, cl.Atom):
        for ele in a:
            if operation == "-":
                if reverse == False:
                    oper.append(list(np.asarray(b.position) - np.asarray(ele)))
                else:
                    oper.append(list(np.asarray(ele) - np.asarray(b.position)))
            elif operation == "+":
                oper.append(list(np.asarray(b.position) - np.asarray(ele)))
    else:
        for ele in a:
            if operation == "-":
                if isinstance(ele, int) or isinstance(ele, float):
                    ele = np.asarray([ele])
                if reverse == False:
                    oper.append(list(np.asarray(b) - ele))
                else:
                    oper.append(list(ele - np.asarray(b)))
            elif operation == "+":
                oper.append(list(np.asarray(b) - np.asarray(ele)))
        return np.array(oper)

def minkowski_distance_p(x, y, p=2):
    x = np.asarray(x)
    y = np.asarray(y)
    if p == np.inf:
        return np.amax(np.abs(y-x), axis=-1)
    elif p == 1:
        return np.sum(np.abs(y-x), axis=-1)
    else:
        return np.sum(np.abs(y-x)**p, axis=-1)


def minkowski_distance(x, y, p=2):
    x = np.asarray(x)
    y = np.asarray(y)
    if p == np.inf or p == 1:
        return minkowski_distance_p(x, y, p)
    else:
        return minkowski_distance_p(x, y, p)**(1./p)

class Rectangle(object):
    """Hyperrectangle class.

    Represents a Cartesian product of intervals.
    """
    def __init__(self, maxes, mins):
        """Construct a hyperrectangle."""
        self.maxes = np.maximum(maxes,mins).astype(np.float)
        self.mins = np.minimum(maxes,mins).astype(np.float)
        self.m, = self.maxes.shape

    def __repr__(self):
        return "<Rectangle %s>" % list(zip(self.mins, self.maxes))

    def volume(self):
        """Total volume."""
        return np.prod(self.maxes-self.mins)

    def split(self, d, split):
        """
        Produce two hyperrectangles by splitting.

        In general, if you need to compute maximum and minimum
        distances to the children, it can be done more efficiently
        by updating the maximum and minimum distances to the parent.

        Parameters
        ----------
        d : int
            Axis to split hyperrectangle along.
        split :
            Input.

        """
        mid = np.copy(self.maxes)
        mid[d] = split
        less = Rectangle(self.mins, mid)
        mid = np.copy(self.mins)
        mid[d] = split
        greater = Rectangle(mid, self.maxes)
        return less, greater

    def min_distance_point(self, x):
        """
        Return the minimum distance between input and points in the hyperrectangle.

        Parameters
        ----------
        x : array_like
            Input.
        """
        try:
            x = x.ravel()[0]
        except AttributeError:
            pass

        if isinstance(x,cl.Atom):
            zero = np.empty(self.m, dtype=np.float)
            zero.fill(0.0)
            return f.euclideanDistance(zero, np.maximum(0, np.maximum(self.mins - x.position, x.position-self.maxes)))
        else:
            a = defyingDimensions("-", x, self.mins)
            b = defyingDimensions("-", x, self.maxes, reverse=True)
            zero = np.empty(self.m, dtype=np.float)
            zero.fill(0.0)
            return f.euclideanDistance(zero, np.maximum(0, np.maximum(a, b)))


    def max_distance_point(self, x):
        """
        Return the maximum distance between input and points in the hyperrectangle.

        Parameters
        ----------
        x : array_like
            Input array.
        """
        if not (isinstance(x, list) or isinstance(x, tuple) or isinstance(x, cl.Atom)):
            "x -> array, other"
            try:
                "x -> array"
                x = x.ravel()
                if not isinstance(x, cl.Atom):
                    x = list(x)
            except AttributeError:
                pass

        if isinstance(x, cl.Atom):
            zero = np.empty(self.m, dtype=np.float)
            zero.fill(0.0)
            return f.euclideanDistance(zero, np.maximum(0, np.maximum(x.position-self.mins, self.maxes - x.position)))
        else:
            a = defyingDimensions("-", x, self.maxes)
            b = defyingDimensions("-", x, self.mins, reverse=True)
            zero = np.empty(self.m, dtype=np.float)
            zero.fill(0.0)
            return f.euclideanDistance(zero, np.maximum(0, np.maximum(a, b)))

    def min_distance_rectangle(self, other):
        """
        Compute the minimum distance between points in the two hyperrectangles.

        Parameters
        ----------
        other : hyperrectangle
            Input.
        """
        zero = np.empty(self.m, dtype=np.float)
        zero.fill(0.0)
        return f.euclideanDistance(zero, np.maximum(zero,np.maximum(self.mins-other.maxes,other.mins-self.maxes)))

    def max_distance_rectangle(self, other):
        """
        Compute the maximum distance between points in the two hyperrectangles.

        Parameters
        ----------
        other : hyperrectangle
            Input.
        p : float, optional
            Input.

        """
        zero = np.empty(self.m, dtype=np.float)
        zero.fill(0.0)
        return f.euclideanDistance(zero, np.maximum(self.maxes-other.mins,other.maxes-self.mins))

class RectangleReal(object):
    """Hyperrectangle class.

    Represents a Cartesian product of intervals.
    """
    def __init__(self, maxes, mins):
        """Construct a hyperrectangle."""
        self.maxes = np.maximum(maxes,mins).astype(np.float)
        self.mins = np.minimum(maxes,mins).astype(np.float)
        self.m, = self.maxes.shape

    def __repr__(self):
        return "<Rectangle %s>" % list(zip(self.mins, self.maxes))

    def volume(self):
        """Total volume."""
        return np.prod(self.maxes-self.mins)

    def split(self, d, split):
        """
        Produce two hyperrectangles by splitting.

        In general, if you need to compute maximum and minimum
        distances to the children, it can be done more efficiently
        by updating the maximum and minimum distances to the parent.

        Parameters
        ----------
        d : int
            Axis to split hyperrectangle along.
        split :
            Input.

        """
        mid = np.copy(self.maxes)
        mid[d] = split
        less = Rectangle(self.mins, mid)
        mid = np.copy(self.mins)
        mid[d] = split
        greater = Rectangle(mid, self.maxes)
        return less, greater

    def min_distance_point(self, x, p=2.):
        """
        Return the minimum distance between input and points in the hyperrectangle.

        Parameters
        ----------
        x : array_like
            Input.
        p : float, optional
            Input.

        """
        return minkowski_distance(0, np.maximum(0,np.maximum(self.mins-x,x-self.maxes)),p)

    def max_distance_point(self, x, p=2.):
        """
        Return the maximum distance between input and points in the hyperrectangle.

        Parameters
        ----------
        x : array_like
            Input array.
        p : float, optional
            Input.

        """
        return minkowski_distance(0, np.maximum(self.maxes-x,x-self.mins),p)

    def min_distance_rectangle(self, other, p=2.):
        """
        Compute the minimum distance between points in the two hyperrectangles.

        Parameters
        ----------
        other : hyperrectangle
            Input.
        p : float
            Input.

        """
        return minkowski_distance(0, np.maximum(0,np.maximum(self.mins-other.maxes,other.mins-self.maxes)),p)

    def max_distance_rectangle(self, other, p=2.):
        """
        Compute the maximum distance between points in the two hyperrectangles.

        Parameters
        ----------
        other : hyperrectangle
            Input.
        p : float, optional
            Input.

        """
        return minkowski_distance(0, np.maximum(self.maxes-other.mins,other.maxes-self.mins),p)


def testMin_MaxRectangles():
    """
    rect1 <Rectangle [(-13.933999999999999, 7.113500000000001), (5.1520000000000001, 23.180500000000002), (28.408999999999999, 51.857249999999993)]>
    rect2 <Rectangle [(12.375375000000002, 17.637250000000002), (15.032999999999999, 23.180500000000002), (42.768000000000001, 51.857249999999993)]>
    rect1.min_distance_rectangle(rect2) 5.261875
    rect1.max_distance_rectangle(rect2) 43.2618893124
    rect2.min_distance_rectangle(rect1) 5.261875
    rect2.max_distance_rectangle(rect1) 43.2618893124
    :return:
    """
    maxes1 = np.array([-13.933999999999999, 5.1520000000000001,  28.408999999999999])
    mins1  = np.array([ 7.113500000000001,  23.180500000000002,  51.857249999999993])

    maxes2 = np.array([17.637250000000002, 23.180500000000002, 51.857249999999993])
    mins2 = np.array([12.375375000000002, 15.032999999999999, 42.768000000000001, ])


    rect1ATOM = Rectangle(maxes1, mins1)
    rect2ATOM = Rectangle(maxes2, mins2)

    rect1 = RectangleReal(maxes1, mins1)
    rect2 = RectangleReal(maxes2, mins2)

    print "min rect:", rect1ATOM.min_distance_rectangle(rect2ATOM)
    print "kd rect MIN:", rect1.min_distance_rectangle(rect2)
    print "kdProg:", 5.261875, "\n"

    print "max rect 1:", rect1ATOM.max_distance_rectangle(rect2ATOM)
    print "kd rect MAX:", rect1.max_distance_rectangle(rect2)
    print "kdProg:", 43.2618893124


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
def testAgain():
    cys = (55.605, 43.497, 41.101)
    glu = (66.869, 46.233, 42.087)
    computed = euclideanDistance(cys, glu)
    actual = ((cys[0] - glu[0])**2. + (cys[1] - glu[1])**2. + (cys[2] - glu[2])**2.)**(1/2.)


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

testMin_MaxRectangles()
"""
kdtree4atoms : kdtree file from scipy.spatial changed to take PDB's atom objects as points
"""
# Copyright Anne M. Archibald 2008
# Released under the scipy license
from __future__ import division, print_function, absolute_import

import sys
import numpy as np
from heapq import heappush, heappop
import functions as f
import Classes as cl
# import scipy

__all__ = ['indexHelper', 'minmaxBC', 'nonzeroBC', 'allBC', 'maximumBC',
           'defyingDimensions', 'distance_matrix', 'Rectangle', 'KDTree4Atoms']


def indexHelper(i, atom):

    if i==0: return atom.x
    elif i==1: return atom.y
    elif i==2: return atom.z
    else: raise Warning

def minmaxBC(atoms, d=""):
    """
    Finds largest coordinate value based on a chosen index
    :param atoms: atoms to compare
    :param d: coordinate to compare (index)
    :return: array of minimums and maximums
    """
    if d == "":
        d = [0,1,2]
    if isinstance(d,int):
        if d==0:
            maxes = atoms[0].x
            mins = atoms[0].x
        elif d==1:
            maxes = atoms[0].y
            mins = atoms[0].y
        elif d==2:
            maxes = atoms[0].z
            mins = atoms[0].z
    elif isinstance(d,list) or isinstance(d,tuple):
        mins = list(atoms[0].position)
        maxes = list(mins)
    else:
        raise Warning
    for atom in atoms:
        if isinstance(d, int):
            if indexHelper(d,atom) < mins:
                mins = indexHelper(d,atom)
            if indexHelper(d,atom) > maxes:
                maxes = indexHelper(d,atom)
        elif isinstance(d, list) or isinstance(d, tuple):
            for j in d:
                if indexHelper(j,atom) < mins[j]:
                    mins[j] = indexHelper(j,atom)
                if indexHelper(j,atom) > maxes[j]:
                    maxes[j] = indexHelper(j,atom)
    return np.asarray(mins), np.asarray(maxes)

def nonzeroBC(comp, data, compVal, d=list([0,1,2])):
    """
    Uses nonzero method concept from NumPy on atom objects
    :param comp: equality sign
    :param data: data to compare
    :param compVal: value to compare
    :param d: indices/index (coordinate of atom)
    :return:
    """
    facts = []
    for a in range(len(data)):
        if isinstance(d,list) or isinstance(d, tuple):
            for i in d:
                if comp == "<":
                    if indexHelper(i,data[a]) < compVal:
                        facts.append(a)
                elif comp == ">":
                    if indexHelper(i,data[a]) > compVal:
                        facts.append(a)
                elif comp == "<=":
                    if indexHelper(i,data[a]) <= compVal:
                        facts.append(a)
                elif comp == ">=":
                    if indexHelper(i,data[a]) >= compVal:
                        facts.append(a)
                elif comp == "==":
                    if indexHelper(i,data[a]) == compVal:
                        facts.append(a)
                else:
                    raise Warning
        else:
            raise Warning
    return facts

def returnMatches(data, idx):
    """
    :param data: array of data
    :param idx: array of indices
    :return: array containing data at indices
    """
    DATA = []
    for i in idx:
        try:
            DATA.append(data[i])
        except:
            raise Warning
    return DATA

def allBC(comp, data, compVal, d):
    """
    :param comp: comparison symbol in form of str
    :param data: list of atoms
    :param compVal: float
    :param d: index
    :return: boolean
    """
    compVal = tuple(compVal)
    for atom in data:
        if comp == "==":
            if indexHelper(d, atom.position) != compVal:
                return False
        elif comp == "<":
            if indexHelper(d, atom.position) >= compVal:
                return False
        elif comp == ">":
            if indexHelper(d, atom.position) <= compVal:
                return False
        elif comp == "<=":
            if indexHelper(d, atom.position) > compVal:
                return False
        elif comp == ">=":
            if indexHelper(d, atom.position) < compVal:
                return False
        else:
            raise Warning
    return True

def maximumBC(pt1, pt2):
    """
    Finds largest point (integer)
    :param pt1: one integer or list of integers
    :param pt2: one integer or list of integers
    :return: largest point
    """
    max = []
    i = ""
    j = ""
    if isinstance(pt1, int):
        if isinstance(pt2, int):
            if pt1 >= pt2:
                return pt1
            else:
                return pt2
        else:
            i = "int"
    elif isinstance(pt2, int): j = "int"
    if len(pt1) == len(pt2):
        for cord in range(len(pt1)):
            if pt1[cord] >= pt2[cord]:
                max.append(pt1[cord])
            else:
                max.append(pt2[cord])
    if i=="int":
        for cord in pt2:
            if cord >= pt1:
                max.append(cord)
            else:
                temp = []
                for c in range(len(pt2)):
                    temp.append(pt1)
                max.append(np.asarray(temp))
    if j=="int":
        for cord in pt1:
            if cord >= pt2:
                max.append(cord)
            else:
                temp = []
                for c in range(len(pt1)):
                    temp.append(pt2)
                max.append(np.asarray(temp))
    else:
        raise Warning
    return tuple(max)

def defyingDimensions(operation, a, b, reverse=False):
    """
    Solves expression with elements that have different dimensions (To work like NumPy)
    :param operation: operation (string)
    :param a: operand 1
    :param b: operand 2
    :param reverse: boolean that determines if operation needs to be solved in reverse order
    :return:
    """
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

def qualifyingHelper(a, dist, distance_upper_bound, orEqual, atomName, res):
    """
    Recursive function that compares a list with a single atom and determines which are qualified pairs and returns a
    list of booleans
    :param a: array of atom object
    :param dist: array/list of euclidean distances between all atom objects from one node and one atom object from the
                 other node
    :param distance_upper_bound: distance limit
    :param orEqual: equality sign as a string
    :param atomName: atom name
    :param res: residue name
    :return: array of booleans boolean
    """
    qualified = []
    if len(a) == 1:
        return isQualified(a, dist, distance_upper_bound, orEqual, atomName, res)
    if isinstance(a[0], cl.Atom):
        D = dist
        for at in range(len(a)):
            if D != "":
                D = dist[at]
            qualified.append(isQualified(a[at], D, distance_upper_bound, orEqual, atomName, res))
    else:
        raise Warning
    return np.asarray(qualified)

def isQualifiedHelper(a, dist="", distance_upper_bound="", orEqual="", atomName="", res=""):
    """
    Loops through all atoms in atom 2 and creates a 2D-array :
        - TYPE: list of lists of booleans
        - Each list relates to an atom in atom 2

    :param a: array of atom object or single atom object
    :param dist: array/list of euclidean distances between all atom objects from one node and one atom object from the
                 other node
    :param distance_upper_bound: atom 2 list of distance limits (in order) *
    :param orEqual: equality sign as a string
    :param atomName: atom 2 list of name (in order) *
    :param res: residue name for atom 2
    :return: 2D array of booleans
    """
    qualified = []
    for a in range(len(atomName)):
        qualified.append(isQualified(a=a, dist=dist, distance_upper_bound=distance_upper_bound[a], orEqual="==", atomName=atomName[a], res=res))
    return qualified




def isQualified(a, dist="", distance_upper_bound="", orEqual="", atomName="", res=""):
    """
    Determines if pair has all the correct requirements
    :param a: atom object
    :param dist: array/list of euclidean distances between all atom objects from one node and one atom object from the
                 other node
    :param distance_upper_bound: distance limit
    :param orEqual: equality sign as a string
    :param atomName: atom name
    :param res: residue name
    :return: boolean
    """

    if len(distance_upper_bound) != atomName:
        raise Warning("IsQualified: Incomplete data regarding atom 2")
    if len(distance_upper_bound) > 1 and len(atomName) > 1:
        return isQualifiedHelper(a, dist, distance_upper_bound, orEqual, atomName, res)
    elif not isinstance(a, cl.Atom):
        if len(a) > 1:
            return qualifyingHelper(a, dist, distance_upper_bound, orEqual, atomName, res)
        elif len(a) == 1:
            a = a[0]
            if dist != "":
                if type(dist) != float:
                    print(type(dist))
                    dist = dist[0]
            return isQualified(a, dist, distance_upper_bound, orEqual, atomName, res)
        else:
            raise Warning("IsQualified: There are no atom objects to compare")
    else:
        if not isinstance(dist, str):
            dist = float(dist)
        if not isinstance(distance_upper_bound, str):
            distance_upper_bound = float(distance_upper_bound)
        if (dist != "" and distance_upper_bound != "") and ((dist >= distance_upper_bound and orEqual=="") or (dist > distance_upper_bound and orEqual=="=")):
            return False
        if atomName != "" and a.name != atomName:
            return False
        if res != "" and a.resName != res:
            return False
        return True


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
            return f.euclideanDistance(zero, np.maximum(0, np.maximum(self.maxes-x.position,x.position-self.mins)))   #x.position-self.mins, self.maxes - x.position
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


class KDTree4Atoms(object):
    """
    kd-tree for quick nearest-neighbor lookup
    This class provides an index into a set of k-dimensional points which
    can be used to rapidly look up the nearest neighbors of any point.
    Parameters
    ----------
    data : (N,K) array_like
        The data points to be indexed. This array is not copied, and
        so modifying this data will result in bogus results.
    leafsize : int, optional
        The number of points at which the algorithm switches over to
        brute-force.  Has to be positive.
    Raises
    ------
    RuntimeError
        The maximum recursion limit can be exceeded for large data
        sets.  If this happens, either increase the value for the `leafsize`
        parameter or increase the recursion limit by::
            >>> import sys
            >>> sys.setrecursionlimit(10000)
    Notes
    -----
    The algorithm used is described in Maneewongvatana and Mount 1999.
    The general idea is that the kd-tree is a binary tree, each of whose
    nodes represents an axis-aligned hyperrectangle. Each node specifies
    an axis and splits the set of points based on whether their coordinate
    along that axis is greater than or less than a particular value.
    During construction, the axis and splitting point are chosen by the
    "sliding midpoint" rule, which ensures that the cells do not all
    become long and thin.
    The tree can be queried for the r closest neighbors of any given point
    (optionally returning only those within some maximum distance of the
    point). It can also be queried, with a substantial gain in efficiency,
    for the r approximate closest neighbors.
    For large dimensions (20 is already large) do not expect this to run
    significantly faster than brute force. High-dimensional nearest-neighbor
    queries are a substantial open problem in computer science.
    The tree also supports all-neighbors queries, both with arrays of points
    and with other kd-trees. These do use a reasonably efficient algorithm,
    but the kd-tree is not necessarily the best data structure for this
    sort of calculation.
    """
    def __init__(self, atoms, leafsize=10):
        self.data = np.asarray(atoms)
        self.n = np.shape(self.data)[0]
        self.m = np.shape(np.asarray(atoms[0].position))[0]
        self.leafsize = int(leafsize)
        if self.leafsize < 1:
            raise ValueError("Leafsize must be at least 1")
        self.mins, self.maxes = minmaxBC(atoms)
        self.tree = self.__construct(np.arange(self.n), self.maxes, self.mins)

    class node(object):
        if sys.version_info[0] >= 3:
            def __lt__(self, other):
                id(self) < id(other)

            def __gt__(self, other):
                id(self) > id(other)

            def __le__(self, other):
                id(self) <= id(other)

            def __ge__(self, other):
                id(self) >= id(other)

            def __eq__(self, other):
                id(self) == id(other)

    class leafnode(node):
        def __init__(self, idx, resis):
            self.idx = np.asarray(idx)
            self.children = len(idx)
            self.resi = resis

    class innernode(node):
        def __init__(self, split_dim, split, less, greater):
            self.split_dim = split_dim
            self.split = split
            self.less = less
            self.greater = greater
            self.children = less.children+greater.children

    def residues(self, idx):
        reses = set()
        for i in self.data[idx]:
            reses.add(i.resName)
        return reses

    def __construct(self, idx, maxes, mins):
        if len(idx) <= self.leafsize:
            return KDTree4Atoms.leafnode(idx, self.residues(idx))
        else:
            data = self.data[idx]
            # maxes = np.amax(data,axis=0)
            # mins = np.amin(data,axis=0)
            d = np.argmax(maxes-mins)
            try:
                maxval = maxes[d]
                minval = mins[d]
            except:
                raise Warning
            if maxval == minval:
                # all points are identical; warn user?

                return KDTree4Atoms.leafnode(idx, self.residues(idx))

            # sliding midpoint rule; see Maneewongvatana and Mount 1999
            # for arguments that this is a good idea.
            split = (maxval+minval)/    2
            less_idx = nonzeroBC("<=", data, split, [int(d)])
            greater_idx = nonzeroBC(">", data, split, [int(d)])
            if len(less_idx) == 0:
                split, blank = minmaxBC(data, int(d))
                less_idx = nonzeroBC("<=", data, split, [int(d)])
                greater_idx = nonzeroBC(">", data, split, [int(d)])
            if len(greater_idx) == 0:
                blank, split = minmaxBC(data, int(d))
                less_idx = nonzeroBC("<", data, split, [int(d)])
                greater_idx = nonzeroBC(">=", data, split, [int(d)])
            if len(less_idx) == 0:
                # _still_ zero? all must have the same value
                if not allBC("==", data, data[0], int(d)):
                    raise ValueError("Troublesome data array: %s" % data)
                split = indexHelper(d, data[0])
                less_idx = np.arange(len(data)-1)
                greater_idx = np.array([len(data)-1])

            lessmaxes = np.copy(maxes)
            lessmaxes[d] = split
            greatermins = np.copy(mins)
            greatermins[d] = split
            return KDTree4Atoms.innernode(d, split,
                    self.__construct(returnMatches(idx, less_idx), lessmaxes,mins),
                    self.__construct(returnMatches(idx, greater_idx), maxes,greatermins))

    def addMoreAtoms(self, Atoms):

        self.data = list(self.data)
        if isinstance(Atoms, cl.Atom):
            self.data.append(Atoms)
        elif len(Atoms) > 1:
            for a in Atoms:
                self.data.append(Atoms)
        return self.__init__(self.data, self.leafsize)

    def __query(self, x, res="", atomName="", k=1, eps=0, distance_upper_bound=np.inf, neighbors=list(), K=""):
        if isinstance(x,cl.Atom):
            side_distances = np.maximum(0, np.maximum(x.position-self.maxes, self.mins-x.position))
        else:
            raise Warning
        # else:
        #     side_distances = np.maximum(0,np.maximum(defyingDimensions("-", x, self.maxes),defyingDimensions("-", self.mins, x, True)))
        side_distances **= 2
        min_distance = np.sum(side_distances)
        # priority queue for chasing nodes
        # entries are:
        #  minimum distance between the cell and the target
        #  distances between the nearest side of the cell and the target
        #  the head node of the cell
        q = [(min_distance,
              tuple(side_distances),
              self.tree)]
        # priority queue for the nearest neighbors
        # furthest known neighbor first
        # entries are (-distance**p, i)
        # neighbors = []

        if eps == 0:
            epsfac = 1
        else:
            epsfac = 1/(1+eps)**2

        if distance_upper_bound != np.inf:
            if K == "":
            #   "Regular use of query"
                distance_upper_bound = distance_upper_bound ** 2
            else:
                for c in range(K, k):
                    distance_upper_bound[c] = distance_upper_bound[c] ** 2

        while q:
            if K != "":
                if len(neighbors) == k:
                    return neighbors

            min_distance, side_distances, node = heappop(q)
            if isinstance(node, KDTree4Atoms.leafnode):
                # brute-force
                if res in node.resi:
                    data = self.data[node.idx]
                    if not isinstance(x, cl.Atom):
                        " Check "
                        print("More than one atom object in __query")
                    if len(data) == 1:
                        ds = []
                        ds.append(f.euclideanDistance(data, x.position))
                    else:
                        ds = f.euclideanDistance(data, x.position)
                    ds = np.asarray(ds)
                    for i in range(len(ds)):
                        if K == "":
                            "Regular use of query"
                            if isQualified(data, ds[i], distance_upper_bound, atomName=atomName, res=res) == True:
                                if len(neighbors) == k:
                                    heappop(neighbors)
                                heappush(neighbors, (-ds[i], i))
                                if len(neighbors) == k:
                                    distance_upper_bound = neighbors[0][0]
                        else:
                            "query_pairs using query"
                            w = 0
                            for ele in atomName:
                                qualified = isQualified(data[i], ds[i], distance_upper_bound[w], atomName=ele,res=res)
                                if qualified == True:
                                    heappush(neighbors, (ele, i))
                                    atomName.pop(w)
                                    distance_upper_bound.pop(w)
                                    if len(neighbors) == k:
                                        return neighbors
                                    else:
                                        break
                                w += 1

            else:
                # we don't push cells that are too far onto the queue at all,
                # but since the distance_upper_bound decreases, we might get
                # here even if the cell's too far
                if K == "":
                    if min_distance > distance_upper_bound*epsfac:
                        # since this is the nearest cell, we're done, bail out
                        break
                else:
                    if np.all(min_distance > distance_upper_bound*epsfac):
                        # since this is the nearest cell, we're done, bail out
                        break

                # compute minimum distances to the children and push them on
                if x.position[node.split_dim] < node.split:
                    near, far = node.less, node.greater
                else:
                    near, far = node.greater, node.less

                # near child is at the same distance as the current node
                heappush(q,(min_distance, side_distances, near))

                # far child is further by an amount depending only
                # on the split value
                sd = list(side_distances)
                sd[node.split_dim] = (node.split-x.position[node.split_dim])**2.
                min_distance -= side_distances[node.split_dim] + sd[node.split_dim]

                # far child might be too far, if so, don't bother pushing it
                if K == "":
                    if min_distance <= distance_upper_bound*epsfac:
                        heappush(q, (min_distance, tuple(sd), far))
                else:
                    if epsfac == 1:
                        if np.all(min_distance <= distance_upper_bound):
                            heappush(q, (min_distance, tuple(sd), far))
                    else:
                        testing = [p*epsfac for p in distance_upper_bound]
                        if np.all(min_distance <= testing):
                            heappush(q, (min_distance, tuple(sd), far))

        # return sorted(neighbors)
        # return [p**(1./2.) for (atm, p) in neighbors]
        # if atomName != []:
        #     print("didn't fill")
        return neighbors

    def query(self, x, res="", atomName="", k=1, eps=0, distance_upper_bound=np.inf, K="", neighbors=list()):
        """
        Query the kd-tree for nearest neighbors
        Parameters
        ----------
        x : array_like, last dimension self.m
            An array of points to query.
        k : integer
            The number of nearest neighbors to return.
        eps : nonnegative float
            Return approximate nearest neighbors; the kth returned value
            is guaranteed to be no further than (1+eps) times the
            distance to the real kth nearest neighbor.
        p : float, 1<=p<=infinity
            Which Minkowski p-norm to use.
            1 is the sum-of-absolute-values "Manhattan" distance
            2 is the usual Euclidean distance
            infinity is the maximum-coordinate-difference distance
        distance_upper_bound : nonnegative float
            Return only neighbors within this distance. This is used to prune
            tree searches, so if you are doing a series of nearest-neighbor
            queries, it may help to supply the distance to the nearest neighbor
            of the most recent point.
        Returns
        -------
        d : array of floats
            The distances to the nearest neighbors.
            If x has shape tuple+(self.m,), then d has shape tuple if
            k is one, or tuple+(k,) if k is larger than one.  Missing
            neighbors are indicated with infinite distances.  If k is None,
            then d is an object array of shape tuple, containing lists
            of distances. In either case the hits are sorted by distance
            (nearest first).
        i : array of integers
            The locations of the neighbors in self.data. i is the same
            shape as d.
        # Examples
        # --------
        # >>> from scipy import spatial
        # >>>
        # >>> tree = spatial.KDTree4Atoms(zip(x.ravel(), y.ravel()))
        # >>> tree.data
        """

        "Use query instead of just __query because query includes checking size of x"
        if isinstance(x,list):
            if len(x[0]) == 1:
                x = "newFunction"
            else:
                numAtoms = len(x[0])
                x = np.empty(numAtoms, dtype=np.object)
                for ob in np.ndindex(numAtoms):
                    x[ob] = "newFunction"
        try:
            product = len(x[0].position)
        except:
            product = len(x.position)
        if product != self.m:
            raise ValueError("x must consist of vectors of length %d but has shape %s" % (self.m, product))
        if K!="":
            hits = self.__query(x, res=res, atomName=atomName, k=k, eps=eps, distance_upper_bound=distance_upper_bound, K=K,
                                neighbors=neighbors)
            return hits
        "But skips making empty arrays"


        retshape = np.shape(x)[:-1]
        if retshape != ():
            if k is None:
                dd = np.empty(retshape,dtype=np.object)
                ii = np.empty(retshape,dtype=np.object)
                atms = np.empty(retshape, dtype=np.object)
            elif k > 1:
                dd = np.empty(retshape+(k,),dtype=np.float)
                dd.fill(np.inf)
                ii = np.empty(retshape+(k,),dtype=np.int)
                ii.fill(self.n)
                atms = np.empty(retshape + (k,), dtype=np.object)
            elif k == 1:
                dd = np.empty(retshape,dtype=np.float)
                dd.fill(np.inf)
                ii = np.empty(retshape,dtype=np.int)
                ii.fill(self.n)
                atms = np.empty(retshape, dtype=np.object)
            else:
                raise ValueError("Requested %s nearest neighbors; acceptable numbers are integers greater than or equal to one, or None")
            for c in np.ndindex(retshape):
                # x[c].ravel()[0] ??
                hits = self.__query(x[c].ravel(), res, atomName, k=k, eps=eps, distance_upper_bound=distance_upper_bound, K=K, neighbors=neighbors)
                if k is None:
                    dd[c] = [d for (d,i) in hits]
                    ii[c] = [i for (d,i) in hits]
                    atms[c] = [self.data[i] for (d,i) in hits]
                elif k > 1:
                    for j in range(len(hits)):
                        dd[c+(j,)], ii[c+(j,)] = hits[j]
                        atms[c] = self.data[ii[c+(j,)]]
                elif k == 1:
                    if len(hits) > 0:
                        dd[c], ii[c] = hits[0]
                        atms[c] = self.data[ii[c]]
                    else:
                        dd[c] = np.inf
                        ii[c] = self.n
                return dd, ii

        else:
            hits = self.__query(x, res, atomName, k=k, eps=eps, distance_upper_bound=distance_upper_bound,K=K,neighbors=neighbors)
            if K!="":
                # USED IN QUERY_PAIRS
                return set(hits)
            if k is None:
                return [self.data[i] for (d,i) in hits]#, [d for (d,i) in hits], [i for (d,i) in hits]
            elif k == 1:
                if len(hits) > 0:
                    return self.data[hits[0][1]]#, hits[0][0], hits[0][1],
                else:
                    return np.inf, self.n
            elif k > 1:
                dd = np.empty(k,dtype=np.float)
                dd.fill(np.inf)
                ii = np.empty(k,dtype=np.int)
                ii.fill(self.n)
                atms = np.empty(k, dtype=np.object)
                for j in range(len(hits)):
                    dd[j], ii[j] = hits[j]
                    atms[j] = self.data[ii[j]]

                # return atms#, dd, ii
            else:
                raise ValueError("Requested %s nearest neighbors; acceptable numbers are integers greater than or equal to one, or None")

    def query_pairs(self, r, res1="", atomName1="", res2="", atomName2="", K=0, eps=0):
        """
        ** Motif connection **
        Greedy search -> stops when algorithm finds all the atoms necessary
        Find a pair of atom objects that are within a specified distance (one for atom 1 and one for an atom in atom 2),
        then implements query to find the other atoms in atom 2 near atom 1

        Parameters
        ----------
        r : list of positive float
            The maximum distance.
        res1 : residue name of main atom
        atomName1 : main atom name
        res2 : residue being compared
        atomName2 : list of atom names to compare
        K : index in set of constraints
        eps : float, optional (IS NOT USED FOR THIS CASE)
            Approximate search.  Branches of the tree are not explored
            if their nearest points are further than ``r/(1+eps)``, and
            branches are added in bulk if their furthest points are nearer
            than ``r * (1+eps)``.  `eps` has to be non-negative.
        Returns
        -------
        results : set()
            pairs (atom name of constraint, index of a constraint)
        """


        # pairs = np.array([[876, 1250], [43, 48], [2872, 2910], [43, 1030], [3363, 3368], [1250, 1450], [450, 48],
        #                   [4350, 3363], [1250, 1212], [1250, 1107], [5375, 5028]])
        # global results

        results = list()

        if len(atomName2) > 1:
                raise Warning("LOCI: kdtree4atoms.py -> query_pairs -> "
                          "traverse_checking \n"
                          "ISSUE: There are not multiple atoms in atom 2")
        if len(r) != len(atomName2):
            raise Warning("LOCI: kdtree4atoms.py -> query_pairs -> "
                                "traverse_checking \n"
                          "ISSUE: Distance parameter r and atom 2 have"
                                "different sizes")


        def traverse4Pair(r, res1, atomName1, res2, atomName2, node1, node2, rect1 = "", rect2= ""):
            """

            :param r:
            :param res1:
            :param atomName1:
            :param res2:
            :param atomName2:
            :param node1:
            :param node2:
            :param rect1:
            :param rect2:
            :return:
            """
            if isinstance(rect1, str) and isinstance(rect2, str):
                pass
            elif isinstance(rect1, Rectangle) and isinstance(rect2, Rectangle):
                pass
            else:
                raise Warning("LOCI: kdtree4atoms -> ")


        def whichCase(caseNum):
            """
            Gives description to the current case by its case number

            :param caseNum: the case number that indicates if the nodes are checked, if the two nodes are the same,
             and where the residues are found
            :return: description string
            """

            # checking
            if caseNum == 1:
                return "LOCI: traverse_checking -> case 1: \n " \
                       "\tnode 1 == node 2 \n" \
                       "\t\tres1 && res2 in node1.resi\n" \
                       "\t\tres1 && res2 in node2.resi"

            if caseNum == 2:
                return "LOCI: traverse_checking -> case 2:" \
                       "\tnode 1 != node 2\n" \
                       "\t\tres1 in node1.resi" \
                       "\t\tres2 in node2.resi"

            if caseNum == 3:
                return "LOCI: traverse_checking -> case 3" \
                       "\tnode 1 != node 2\n" \
                       "\t\tres2 in node1.resi" \
                       "\t\tres1 in node2.resi"

            # no checking
            if caseNum == 4:
                return "LOCI: traverse_no_checking -> case 1: \n " \
                       "\tnode 1 == node 2 \n" \
                       "\t\tres1 && res2 in node1.resi\n" \
                       "\t\tres1 && res2 in node2.resi"
            if caseNum == 5:
                return "LOCI: traverse_no_checking -> case 2:" \
                       "\tnode 1 != node 2\n" \
                       "\t\tres1 in node1.resi" \
                       "\t\tres2 in node2.resi"
            if caseNum == 6:
                return "LOCI: traverse_no_checking -> case 3" \
                       "\tnode 1 != node 2\n" \
                       "\t\tres2 in node1.resi" \
                       "\t\tres1 in node2.resi"


        def traverse_checking(node1, rect1, node2, rect2):
            """
            1. Compares the rectangles with the distance constraints (If all possible pairs are greater than the
                distance bounds given, it skips those nodes)
            2. Traverses through nodes in a kdtree and looks through the leafnodes
            3. Determines which atoms in the node in one node match with which atoms in the second node are qualified
               pairs
            4. Loop through a node that has atom 1
            5. Makes a 2D array of booleans that represent which atoms are qualified as an atom in atom 2
            6. Loop through possible pairs and implement query to find the rest of the cluster
            7. If algorithm found entire cluster, return cluster. If not, empty results and continue traversing


            :param node1: a node in the kdtree
            :param node2: a node in the kdtree
            :return:
            """
            if results != []:
                return

            # if isinstance(r,list):
            #     R = r[K]
            # else:
            #     R = r

            if np.all(rect1.min_distance_rectangle(rect2) > np.asarray(r)/(1.+eps)):
                return
            elif np.all(rect1.max_distance_rectangle(rect2) < np.asarray(r)*(1.+eps)):
                traverse_no_checking(node1, node2)
            elif isinstance(node1, KDTree4Atoms.leafnode):
                if isinstance(node2, KDTree4Atoms.leafnode):
                    # Special care to avoid duplicate pairs
                    if id(node1) == id(node2):
                        # K = 0
                        d = self.data[node2.idx]

                        "Case 1a"
                        if res1 in node1.resi and res2 in node1.resi:
                            for i in node1.idx:
                                if self.data[i].name == atomName1 and self.data[i].resName == res1:
                                    if type(r) == list:
                                        isMatrix = True
                                        qualified = isQualified(a=d, dist=f.euclideanDistance(d, self.data[i].position),
                                                                distance_upper_bound=r, orEqual="==", res=res2,
                                                                atomName=atomName2)

                                        # Ensure matrix is correct size
                                        if len(atomName2) != len(qualified):

                                            caseInfo = raw_input("Would you like to know about the case we are in? (y/n)")
                                            if caseInfo == "y":
                                                print(whichCase(1))

                                            raise Warning("Cannot implement query until issue is resolved :\n "
                                                          "\t~ LOCI: query_pairs-> traverse_checking -> Case 1"
                                                          "\t~ Issue: atom 2 and qualified lists are not the same "
                                                          "     size")
                                        for row in range(len(qualified)):
                                            if len(row) != len(d):

                                                caseInfo = raw_input(
                                                    "Would you like to know about the case we are in? (y/n)")
                                                if caseInfo == "y":
                                                    print(whichCase(1))

                                                raise Warning("LOCI: kdtree4atoms -> traverse_checking -> Case 1\n"
                                                              "Issue: qualified parameter is not the same size as the "
                                                              "observed node (d)\n"
                                                              "Row failed: " + row + "\n"
                                                              "Associated atom from atom 2: " + atomName2[row])


                                    else:
                                        isMatrix = False
                                        qualified = isQualified(a=d, dist=f.euclideanDistance(d, self.data[i].position),
                                                                distance_upper_bound=r, orEqual="==", res=res2,
                                                                atomName=atomName2)

                                        if len(qualified) != len(d):

                                            caseInfo = raw_input("Would you like to know about the case we are in? (y/n)")
                                            if caseInfo == "y":
                                                print(whichCase(1))

                                            raise Warning("LOCI: kdtree4atoms -> traverse_checking -> Case 1\n"
                                                          "Issue: qualified parameter is not the same size as the "
                                                          "observed node (d)")

                                    if isinstance(qualified, bool):
                                        qualified = np.asarray([qualified])


                                    # if K == len(atomName2) - 1:
                                    #    if len(results) == 2:
                                    #        if isinstance(results[1], list):
                                    #            if K == len(results[1]) - 1:
                                    #                pass
                                    #            else:
                                    #                raise Warning("Looked through all atom 2")


                                    # jk = np.copy(K)

                                    if isMatrix:
                                        # There are multiple atoms in atom 2
                                        for q in range(len(qualified)):
                                            qual = qualified[q]
                                            for j in node2.idx[qual]:
                                                if isinstance(results, list):

                                                    if type(r) == list:
                                                        if len(atomName2) > 1:
                                                            # Multiple atoms in atom 2
                                                            neighbors = []
                                                            neighbors.append((atomName2[q], j))
                                                            atomsCopy = list(np.copy(atomName2))
                                                            del atomsCopy[q]
                                                            rCopy = np.copy(r)
                                                            collections = self.query(self.data[i], res=res2,
                                                                                     atomName=list(atomsCopy),
                                                                                     k=len(atomName2),
                                                                                     distance_upper_bound=list(rCopy),
                                                                                     K=q, neighbors=neighbors)
                                                            # Successful to find entire cluster near atom 1
                                                            if len(collections) == len(atomName2):
                                                                results.append((atomName1, i))
                                                                results.append(collections)
                                                                return
                                                            # Failure to find entire cluster near atom 1
                                                            else:
                                                                results = []
                                                else:

                                                    caseInfo = raw_input(
                                                        "Would you like to know about the case we are in? (y/n)")
                                                    if caseInfo == "y":
                                                        print(whichCase(1))

                                                    print("results:", results)
                                                    raise Warning("LOCI: traverse_checking (Case 1, part 1): "
                                                                  "ISSUE: Results are not a list")
                                    else:
                                        for j in node2.idx[qualified]:
                                            if isinstance(results, list):

                                                if isinstance(atomName2, list) or isinstance(atomName2, np.ndarray):

                                                    if len(atomName2) > 1:

                                                        caseInfo = raw_input(
                                                            "Would you like to know about the case we are in? (y/n)")
                                                        if caseInfo == "y":
                                                            print(whichCase(1))

                                                        raise Warning("LOCI: traverse_checking (Case 1)\n"
                                                                      "ISSUE: Qualified is not a matrix, but atom 2 has "
                                                                             "more than 1 atoms")

                                                    atomName2 = atomName2[0]

                                                results.append((atomName1, i))
                                                results.append([(atomName2[0], j)])
                                                return
                                            else:

                                                caseInfo = raw_input(
                                                    "Would you like to know about the case we are in? (y/n)")
                                                if caseInfo == "y":
                                                    print(whichCase(1))

                                                print("results:", results)
                                                raise Warning("LOCI: traverse_checking (Case 1, part 2): "
                                                              "ISSUE: Results is not a list")

                                            # else:
                                            #     print("results:", results)
                                            #     raise Warning("Results are not a list")
                                        # if isinstance(r, list):
                                        #     K = int(jk)
                                        #     K += 1
                    else:
                        # K = 0
                        " node1 != node2 "

                        "Case 1b"
                        if res1 in node1.resi and res2 in node2.resi:
                            d = self.data[node2.idx]
                            for i in node1.idx:
                                if self.data[i].name == atomName1 and self.data[i].resName == res1:
                                    if type(r) == list:
                                        isMatrix = True
                                        qualified = isQualified(a=d, dist=f.euclideanDistance(d, self.data[i].position),
                                                                distance_upper_bound=r, orEqual="=", res=res2,
                                                                atomName=atomName2)

                                        if len(atomName2) != len(qualified):

                                            caseInfo = raw_input("Would you like to know about the case we are in? (y/n)")
                                            if caseInfo == "y":
                                                print(whichCase(2))

                                            raise Warning("Cannot implement query until issue is resolved :\n "
                                                          "\t~ Location: query_pairs -> traverse_checking -> Case 2 "
                                                          "\t~ Issue: atom 2 and qualified lists are not the same "
                                                          "     size")
                                        for row in range(len(qualified)):
                                            if len(row) != len(d):

                                                caseInfo = raw_input(
                                                    "Would you like to know about the case we are in? (y/n)")
                                                if caseInfo == "y":
                                                    print(whichCase(2))

                                                raise Warning("LOCI: kdtree4atoms -> traverse_checking -> Case 2\n"
                                                              "Issue: qualified parameter is not the same size as the "
                                                              "observed node (d)\n"
                                                              "Row failed: " + row + "\n"
                                                              "Associated atom from atom 2: " + atomName2[row])

                                    else:
                                        isMatrix = False
                                        qualified = isQualified(a=d, dist=f.euclideanDistance(d, self.data[i].position),
                                                                distance_upper_bound=r, orEqual="=", res=res2,
                                                                atomName=atomName2)
                                        if len(qualified) != len(d):

                                            caseInfo = raw_input("Would you like to know about the case we are in? (y/n)")
                                            if caseInfo == "y":
                                                print(whichCase(2))

                                            raise Warning("LOCI: kdtree4atoms -> traverse_checking -> Case 2\n"
                                                          "Issue: qualified parameter is not the same size as the "
                                                          "observed node (d)")

                                    if isinstance(qualified, bool):
                                        qualified = np.asarray([qualified])


                                    # if K == len(atomName2) - 1:
                                    #    if len(results) == 2:
                                    #        if isinstance(results[1], list):
                                    #            if K == len(results[1]) - 1:
                                    #                pass
                                    #            else:
                                    #                raise Warning("Looked through all atom 2")

                                    # K += 1
                                    # jk = np.copy(K)

                                    if isMatrix:
                                        for q in range(len(qualified)):
                                            qual = qualified[q]

                                            for j in node2.idx[qual]:
                                                if isinstance(results, list):
                                                    if type(r) == list:

                                                        if len(atomName2) > 1:
                                                            # print("Part 2: (res 1) in (node 1) != (res 2) in (node 2) -> \n"
                                                            #         "\tAtom 2 ->", atomName2, "\n"
                                                            #         "\tK -> ", K, "\n")

                                                            neighbors = []
                                                            neighbors.append((atomName2[q], j))
                                                            atomsCopy = list(np.copy(atomName2))
                                                            del atomsCopy[q]
                                                            rCopy = np.copy(r)
                                                            collections = self.query(self.data[i], res=res2,
                                                                                     atomName=list(atomsCopy),
                                                                                     k=len(atomName2),
                                                                                     distance_upper_bound=list(rCopy),
                                                                                     K=q,
                                                                                     neighbors=neighbors)
                                                            if len(collections) == len(atomName2):
                                                                results.append((atomName1, i))
                                                                results.append(collections)
                                                                return
                                                            else:
                                                                results = []
                                                else:
                                                    caseInfo = raw_input(
                                                        "Would you like to know about the case we are in? (y/n)")
                                                    if caseInfo == "y":
                                                        print(whichCase(2))

                                                    print("results:", results, "TYPE:", type(results))
                                                    raise Warning("traverse_checking (Case 2, part 1): Results is not a list")

                                    else:
                                        for j in node2.idx[qualified]:
                                            if isinstance(results, list):

                                                if isinstance(atomName2, list) or isinstance(atomName2, np.ndarray):

                                                    if len(atomName2) > 1:

                                                        caseInfo = raw_input(
                                                            "Would you like to know about the case we are in? (y/n)")
                                                        if caseInfo == "y":
                                                            print(whichCase(2))

                                                        raise Warning("LOCI: traverse_checking (Case 1)\n"
                                                                      "ISSUE: Qualified is not a matrix, but atom 2 has "
                                                                             "more than 1 atoms")

                                                    atomName2 = atomName2[0]


                                                results.append((atomName1, i))
                                                results.append([(atomName2[0], j)])
                                                return
                                                # else:
                                                #     raise Warning("Distance parameter r is not a list")
                                            else:

                                                caseInfo = raw_input(
                                                    "Would you like to know about the case we are in? (y/n)")
                                                if caseInfo == "y":
                                                    print(whichCase(2))

                                                print("results:", results)
                                                raise Warning("traverse_checking (Case 2, part 2): Results is not a list")
                                                # if type(r) == list:
                                                #     K = int(jk)
                                                #     K += 1



                        " Case 1c "
                        if res1 in node2.resi and res2 in node1.resi:
                            # K = 0
                            d = self.data[node1.idx]
                            # Atom 1 in node 2, atom 2 in node 1
                            for j in node2.idx:
                                if self.data[j].name == atomName1 and self.data[j].resName == res1:

                                    if type(r) == list:
                                        isMatrix = True

                                        # Ensure matrix is correct size

                                        if len(atomName2) != len(qualified):

                                            caseInfo = raw_input("Would you like to know about the case we are in? (y/n)")
                                            if caseInfo == "y":
                                                print(whichCase(3))

                                            raise Warning("Cannot implement query until issue is resolved :\n "
                                                          "\t~ Location: query_pairs -> traverse_checking -> Case 3"
                                                          "\t~ Issue: atom 2 and qualified lists are not the same "
                                                          "     size")
                                        for row in range(len(qualified)):
                                            if len(row) != len(d):

                                                caseInfo = raw_input(
                                                    "Would you like to know about the case we are in? (y/n)")
                                                if caseInfo == "y":
                                                    print(whichCase(3))

                                                raise Warning("LOCI: kdtree4atoms -> traverse_checking -> Case 3\n"
                                                              "Issue: qualified parameter is not the same size as the "
                                                                     "observed node (d)\n"
                                                              "Row failed: " + row + "\n"
                                                              "Associated atom from atom 2: " + atomName2[row])



                                    else:
                                        isMatrix = False

                                        if len(qualified) != len(d):

                                            caseInfo = raw_input("Would you like to know about the case we are in? (y/n)")
                                            if caseInfo == "y":
                                                print(whichCase(3))

                                            raise Warning("LOCI: kdtree4atoms -> traverse_checking -> Case 3\n"
                                                          "Issue: qualified parameter is not the same size as the "
                                                          "observed node (d)")

                                    # Reminder: d -> atom 2
                                    qualified = isQualified(a=d, dist=f.euclideanDistance(d, self.data[j].position),
                                                                distance_upper_bound=r, orEqual="=", res=res2,
                                                                atomName=atomName2)


                                    if isinstance(qualified, bool):
                                        qualified = np.asarray([qualified])


                                    # if K == len(atomName2) - 1:
                                    #    if len(results) == 2:
                                    #        if isinstance(results[1], list):
                                    #            if K == len(results[1]) - 1:
                                    #                pass
                                    #            else:
                                    #                raise Warning("Looked through all atom 2")

                                    # K += 1
                                    # jk = np.copy(K)

                                    if isMatrix:
                                        for q in range(len(qualified)):
                                            qual = qualified[q]
                                            for i in node1.idx[qual]:
                                                if isinstance(results, list):

                                                    # print("Part 3: (res 2) in (node 1) != (res 1) in (node 2):  ->
                                                    # \n\tAtom 2: ", atomName2, "\n\tK -> ", K, "\n")

                                                    neighbors = []
                                                    neighbors.append((atomName2[q], i))
                                                    atomsCopy = list(np.copy(atomName2))
                                                    del atomsCopy[q]
                                                    rCopy = np.copy(r)
                                                    collections = self.query(self.data[j], res=res2,
                                                                             atomName=atomsCopy,
                                                                             k=len(atomName2),
                                                                             distance_upper_bound=list(rCopy),
                                                                             K=q,
                                                                             neighbors=neighbors)
                                                    if len(collections) == len(atomName2):
                                                        results.append((atomName1, j))
                                                        results.append(collections)
                                                        return
                                                    else:
                                                        results = []
                                                else:

                                                    caseInfo = raw_input(
                                                        "Would you like to know about the case we are in? (y/n)")
                                                    if caseInfo == "y":
                                                        print(whichCase(3))

                                                    print("results:", results)
                                                    raise Warning("traverse_checking (Case 3, part 1): Results is not a list")
                                                    # if type(r) == list:
                                                    #     K = int(jk)
                                                    #     K += 1
                                    else:

                                        for i in node1.idx[qualified]:
                                            if isinstance(results, list):

                                                if isinstance(atomName2, list) or isinstance(atomName2, np.ndarray):

                                                    if len(atomName2) > 1:

                                                        caseInfo = raw_input(
                                                            "Would you like to know about the case we are in? (y/n)")
                                                        if caseInfo == "y":
                                                            print(whichCase(3))

                                                        raise Warning("LOCI: traverse_checking (Case 3)\n"
                                                                      "ISSUE: Qualified is not a matrix, but atom 2 has "
                                                                      "more than 1 atoms")

                                                    atomName2 = atomName2[0]



                                                results.append((atomName1, j))
                                                results.append([(atomName2, i)])
                                                return
                                            else:

                                                caseInfo = raw_input(
                                                    "Would you like to know about the case we are in? (y/n)")
                                                if caseInfo == "y":
                                                    print(whichCase(3))

                                                print("results:", results)
                                                raise Warning("traverse_checking (Case 3. part 2): Results is not a list")

                else:
                    less, greater = rect2.split(node2.split_dim, node2.split)
                    traverse_checking(node1,rect1,node2.less,less)
                    traverse_checking(node1,rect1,node2.greater,greater)
            elif isinstance(node2, KDTree4Atoms.leafnode):
                less, greater = rect1.split(node1.split_dim, node1.split)
                traverse_checking(node1.less,less,node2,rect2)
                traverse_checking(node1.greater,greater,node2,rect2)
            else:
                less1, greater1 = rect1.split(node1.split_dim, node1.split)
                less2, greater2 = rect2.split(node2.split_dim, node2.split)
                traverse_checking(node1.less,less1,node2.less,less2)
                traverse_checking(node1.less,less1,node2.greater,greater2)

                # Avoid traversing (node1.less, node2.greater) and
                # (node1.greater, node2.less) (it's the same node pair twice
                # over, which is the source of the complication in the
                # original KDTree.query_pairs)
                if id(node1) != id(node2):
                    traverse_checking(node1.greater,greater1,node2.less,less2)

                traverse_checking(node1.greater,greater1,node2.greater,greater2)

        def traverse_no_checking(node1, node2):
            """
            ** Looks through all nodes given **
            1. Traverses through nodes in a kdtree and looks through the leafnodes
            2. Determines which atoms in the node in one node match with which atoms in the second node are qualified
               pairs
            3. Loop through a node that has atom 1
            4. Makes a 2D array of booleans that represent which atoms are qualified as an atom in atom 2
            5. Loop through possible pairs and implement query to find the rest of the cluster
            6. If algorithm found entire cluster, return cluster. If not, empty results and continue traversing


            :param node1: a node in the kdtree
            :param node2: a node in the kdtree
            :return:
            """
            if len(results) > 0:
                return
            if isinstance(node1, KDTree4Atoms.leafnode):
                if isinstance(node2, KDTree4Atoms.leafnode):
                    # Special care to avoid duplicate pairs
                    if id(node1) == id(node2):

                        "Case 2a"
                        if res1 in node1.resi and res2 in node1.resi:
                            d = self.data[node2.idx]
                            # K = 0
                            for i in node1.idx:
                                if self.data[i].name == atomName1 and self.data[i].resName == res1:

                                    if isinstance(r, list):
                                        isMatrix = True

                                        if len(atomName2) != len(qualified):

                                            caseInfo = raw_input(
                                                "Would you like to know about the case we are in? (y/n)")
                                            if caseInfo == "y":
                                                print(whichCase(4))

                                            raise Warning("Cannot implement query until issue is resolved :\n "
                                                          "\t~ LOCI: kdtree4atoms -> query_pairs -> traverse_no_checking"
                                                          "-> Case 1"
                                                          "\t~ Issue: atom 2 and qualified lists are not the same "
                                                          "     size")
                                        for row in range(len(qualified)):
                                            if len(row) != len(d):

                                                caseInfo = raw_input(
                                                    "Would you like to know about the case we are in? (y/n)")
                                                if caseInfo == "y":
                                                    print(whichCase(4))

                                                raise Warning("LOCI: kdtree4atoms -> traverse_no_checking -> Case 1\n"
                                                              "Issue: qualified parameter is not the same size as the "
                                                                     "observed node (d)\n"
                                                              "Row failed: " + row + "\n"
                                                              "Associated atom from atom 2: " + atomName2[row])

                                    else:
                                        isMatrix = False

                                        if len(qualified) != len(d):

                                            caseInfo = raw_input(
                                                "Would you like to know about the case we are in? (y/n)")
                                            if caseInfo == "y":
                                                print(whichCase(4))

                                            raise Warning("LOCI: kdtree4atoms -> traverse_no_checking -> Case 1\n"
                                                          "Issue: qualified parameter is not the same size as the "
                                                          "observed node (d)")

                                    qualified = isQualified(a=d, res=res2, atomName=atomName2)

                                    if isinstance(qualified, bool):
                                        qualified = np.asarray([qualified])


                                    # if K == len(atomName2) - 1:
                                    #    if len(results) == 2:
                                    #        if isinstance(results[1], list):
                                    #            if K == len(results[1]) - 1:
                                    #                pass
                                    #            else:
                                    #                raise Warning("Looked through all atom 2")

                                    # K += 1
                                    # jk = np.copy(K)

                                    if isMatrix:
                                        for q in range(len(qualified)):
                                            qual = qualified[q]

                                            for j in node2.idx[qual]:
                                                if isinstance(results, list):
                                                    # print("Part 4: (res 2) in (node 1) == (res 1) in (node 2):  -> \n\tAtom 2: ", atomName2, "\n\tK -> ", K, "\n")

                                                    neighbors = []
                                                    neighbors.append((atomName2[q], j))
                                                    atomsCopy = list(np.copy(atomName2))
                                                    del atomsCopy[q]
                                                    rCopy = np.copy(r)
                                                    collections = (
                                                        self.query(self.data[i], distance_upper_bound=list(rCopy),
                                                                   res=res2, atomName=list(atomsCopy),
                                                                   k=len(atomName2), K=q, neighbors=neighbors))
                                                    if len(collections) == len(atomName2):
                                                        results.append((atomName1, j))
                                                        results.append(collections)
                                                        return

                                                else:

                                                    caseInfo = raw_input(
                                                        "Would you like to know about the case we are in? (y/n)")
                                                    if caseInfo == "y" or caseInfo == "Y":
                                                        print(whichCase(4))

                                                    print("results:", results)
                                                    raise Warning("LOCI: kdtree4atoms -> traverse_no_checking -> Case 1\n"
                                                                  "ISSUE: Results is not a list")
                                                    # if isinstance(r, list):
                                                    #     K = int(jk)
                                                    #     K += 1
                                    else:
                                        # not a matrix
                                        for j in node2.idx[qualified]:
                                            if isinstance(results, list):

                                                if isinstance(atomName2, list) or isinstance(atomName2, np.ndarray):

                                                    if len(atomName2) > 1:

                                                        caseInfo = raw_input(
                                                            "Would you like to know about the case we are in? (y/n)")
                                                        if caseInfo == "y":
                                                            print(whichCase(3))

                                                        raise Warning("LOCI: traverse_no_checking (Case 1, part 2)\n"
                                                                      "ISSUE: Qualified is not a matrix, but atom 2 has "
                                                                      "more than 1 atoms")

                                                    atomName2 = atomName2[0]
                                                results.append((atomName1, i))
                                                results.append([(atomName2, j)])
                                                return
                                            else:

                                                caseInfo = raw_input(
                                                    "Would you like to know about the case we are in? (y/n)")
                                                if caseInfo == "y":
                                                    print(whichCase(4))

                                                print("results:", results)
                                                raise Warning("traverse_checking (Case 1. part 2): Results is not a list")


                    else:
                        "Case 2b"
                        if res1 in node1.resi and res2 in node2.resi:
                            # K = 0
                            d = self.data[node2.idx]
                            for i in node1.idx:
                                if self.data[i].name == atomName1 and self.data[i].resName == res1:
                                    qualified = isQualified(a=d, res=res2, atomName=atomName2)

                                    if isinstance(r, list):
                                        isMatrix = True

                                        if len(atomName2) != len(qualified):

                                            caseInfo = raw_input(
                                                "Would you like to know about the case we are in? (y/n)")
                                            if caseInfo == "y":
                                                print(whichCase(4))

                                            raise Warning("Cannot implement query until issue is resolved :\n "
                                                          "\t~ LOCI: kdtree4atoms -> query_pairs -> traverse_no_checking"
                                                          "-> Case 2"
                                                          "\t~ Issue: atom 2 and qualified lists are not the same "
                                                          "     size")
                                        for row in range(len(qualified)):
                                            if len(row) != len(d):

                                                caseInfo = raw_input(
                                                    "Would you like to know about the case we are in? (y/n)")
                                                if caseInfo == "y":
                                                    print(whichCase(5))

                                                raise Warning("LOCI: kdtree4atoms -> traverse_no_checking -> Case 1\n"
                                                              "Issue: qualified parameter is not the same size as the "
                                                                     "observed node (d)\n"
                                                              "Row failed: " + str(row) + "\n"
                                                                                          "Associated atom from atom 2: "
                                                              "Associated atom from atom 2: " + atomName2[row])

                                    else:
                                        isMatrix = False

                                        if len(qualified) != len(d):

                                            caseInfo = raw_input(
                                                "Would you like to know about the case we are in? (y/n)")
                                            if caseInfo == "y":
                                                print(whichCase(5))

                                            raise Warning("LOCI: kdtree4atoms -> traverse_no_checking -> Case 2\n"
                                                          "Issue: qualified parameter is not the same size as the "
                                                          "observed node (d)")


                                    if isinstance(qualified, bool):
                                        qualified = np.asarray([qualified])


                                    # if K == len(atomName2) - 1:
                                    #    if len(results) == 2:
                                    #        if isinstance(results[1], list):
                                    #            if K == len(results[1]) - 1:
                                    #                pass
                                    #            else:
                                    #                raise Warning("Looked through all atom 2")

                                    # K += 1
                                    # jk = np.copy(K)

                                    if isMatrix:
                                        for q in range(len(qualified)):
                                            qual = qualified[q]

                                            for j in node2.idx[qual]:
                                                if isinstance(results, list):


                                                    # print("Part 5: (res 1) in (node 1) != (res 2) in (node 2):
                                                    #   -> \n\tAtom 2: ", atomName2, "\n\tK -> ", K, "\n")

                                                    neighbors = []
                                                    neighbors.append((atomName2[q], j))
                                                    atomsCopy = list(np.copy(atomName2))
                                                    del atomsCopy[q]
                                                    rCopy = np.copy(r)
                                                    collections = self.query(self.data[i],
                                                                             distance_upper_bound=list(rCopy),
                                                                             res=res2, atomName=list(atomsCopy),
                                                                             k=len(atomName2), K=q,
                                                                             neighbors=neighbors)
                                                    if len(collections) == len(atomName2):
                                                        results.append((atomName1, i))
                                                        results.append(collections)
                                                        return

                                                else:
                                                    caseInfo = raw_input(
                                                        "Would you like to know about the case we are in? (y/n)")
                                                    if caseInfo == "y":
                                                        print(whichCase(5))

                                                    print("results:", results)
                                                    raise Warning("LOCI: traverse_no_checking (Case 2): "
                                                                  "ISSUE: Results is not a list")
                                    else:
                                        # not a matrix
                                        for j in node2.idx[qualified]:
                                            if isinstance(results, list):

                                                if isinstance(atomName2, list) or isinstance(atomName2, np.ndarray):

                                                    if len(atomName2) > 1:

                                                        caseInfo = raw_input(
                                                            "Would you like to know about the case we are in? (y/n)")
                                                        if caseInfo == "y":
                                                            print(whichCase(5))

                                                        raise Warning("LOCI: traverse_no_checking (Case 2, part 2)\n"
                                                                      "ISSUE: Qualified is not a matrix, but atom 2 has "
                                                                      "more than 1 atoms")

                                                    atomName2 = atomName2[0]
                                                results.append((atomName1, j))
                                                results.append([(atomName2, i)])
                                                return
                                            else:

                                                caseInfo = raw_input(
                                                    "Would you like to know about the case we are in? (y/n)")
                                                if caseInfo == "y":
                                                    print(whichCase(5))

                                                print("results:", results)
                                                raise Warning("traverse_checking (Case 2. part 2): Results is not a list")

                                    # if isinstance(r, list):
                                    #     K = int(jk)\
                                    #     K += 1
                        "Case 2c"
                        if res1 in node2.resi and res2 in node1.resi:
                            # K = 0
                            d = self.data[node1.idx]
                            for j in node2.idx:
                                if self.data[j].name == atomName1 and self.data[j].resName == res1:
                                    qualified = isQualified(a=d, res=res2, atomName=atomName2)

                                    if isinstance(r, list):
                                        isMatrix = True

                                        if len(atomName2) != len(qualified):
                                            caseInfo = raw_input(
                                                "Would you like to know about the case we are in? (y/n)")
                                            if caseInfo == "y":
                                                print(whichCase(6))

                                            raise Warning("Cannot implement query until issue is resolved :\n "
                                                          "\t~ LOCI: kdtree4atoms -> query_pairs -> traverse_no_checking"
                                                          "-> Case 3"
                                                          "\t~ Issue: atom 2 and qualified lists are not the same "
                                                          "     size")
                                        for row in range(len(qualified)):
                                            if len(row) != len(d):

                                                caseInfo = raw_input(
                                                    "Would you like to know about the case we are in? (y/n)")
                                                if caseInfo == "y":
                                                    print(whichCase(6))

                                                raise Warning("LOCI: kdtree4atoms -> traverse_no_checking -> Case 3\n"
                                                              "Issue: qualified parameter is not the same size as the "
                                                                     "observed node (d)\n"
                                                              "Row failed: " + row + "\n"
                                                              "Associated atom from atom 2: " + atomName2[row])

                                    else:
                                        isMatrix = False
                                        if len(qualified) != len(d):
                                            caseInfo = raw_input(
                                                "Would you like to know about the case we are in? (y/n)")
                                            if caseInfo == "y":
                                                print(whichCase(6))
                                            raise Warning("LOCI: kdtree4atoms -> traverse_no_checking -> Case 3\n"
                                                          "Issue: qualified parameter is not the same size as the "
                                                          "observed node (d)")
                                    if isinstance(qualified, bool):
                                        qualified = np.asarray([qualified])
                                    # if K == len(atomName2) - 1:
                                    #    if len(results) == 2:
                                    #        if isinstance(results[1], list):
                                    #            if K == len(results[1]) - 1:
                                    #                pass
                                    #            else:
                                    #                raise Warning("Looked through all atom 2")
                                    if isMatrix:
                                        for q in range(len(qualified)):
                                            qual = qualified[q]
                                            # jk = np.copy(K)
                                            for i in node1.idx[qual]:
                                                if isinstance(results, list):
                                                    if type(r) == list:
                                                        if len(atomName2) > 1:
                                                            # print("Part 6: (res 2) in (node 1) != (res 1) in (node 2):
                                                            #   -> \n\tAtom 2: ", atomName2, "\n\tK -> ", K, "\n")
                                                            neighbors = []
                                                            neighbors.append((atomName2[q], i))
                                                            atomsCopy = list(np.copy(atomName2))
                                                            del atomsCopy[q]
                                                            rCopy = r
                                                            collections = self.query(self.data[j],
                                                                                     distance_upper_bound=list(rCopy),
                                                                                     res=res2, atomName=list(atomsCopy),
                                                                                     k=len(atomName2), K=q,
                                                                                     neighbors=neighbors)
                                                            if len(collections) == len(atomName2):
                                                                results.append((atomName1, j))
                                                                results.append(collections)
                                                                return
                                                        else:
                                                            results.append((atomName1, j))
                                                            results.append([(atomName2[0], i)])
                                                    else:
                                                        raise Warning
                                                else:
                                                    caseInfo = raw_input(
                                                        "Would you like to know about the case we are in? (y/n)")
                                                    if caseInfo == "y":
                                                        print(whichCase(6))

                                                    print("results:", results)
                                                    raise Warning("LOCI: traverse_no_checking (Case 3): "
                                                                  "ISSUE: Results is not a list")
                                                    # results.add((i, j))

                                                    # if isinstance(r, list):
                                                    #     K = int(jk)
                                                    #     K += 1
                                    else:
                                        # not a matrix
                                        for i in node1.idx[qualified]:
                                            if isinstance(results, list):

                                                if isinstance(atomName2, list) or isinstance(atomName2, np.ndarray):

                                                    if len(atomName2) > 1:
                                                        caseInfo = raw_input(
                                                            "Would you like to know about the case we are in? (y/n)")
                                                        if caseInfo == "y":
                                                            print(whichCase(6))

                                                        raise Warning("LOCI: traverse_no_checking (Case 2, part 1)\n"
                                                                      "ISSUE: Qualified is not a matrix, but atom 2 has "
                                                                      "more than 1 atoms")
                                                    atomName2 = atomName2[0]
                                                results.append((atomName1, j))
                                                results.append([(atomName2, i)])
                                                return
                                            else:
                                                caseInfo = raw_input(
                                                    "Would you like to know about the case we are in? (y/n)")
                                                if caseInfo == "y":
                                                    print(whichCase(6))
                                                print("results:", results)
                                                raise Warning("traverse_checking (Case 2. part 2): Results is not a list")



                else:
                    traverse_no_checking(node1, node2.less)
                    traverse_no_checking(node1, node2.greater)
            else:
                # Avoid traversing (node1.less, node2.greater) and
                # (node1.greater, node2.less) (it's the same node pair twice
                # over, which is the source of the complication in the
                # original KDTree.query_pairs)
                if id(node1) == id(node2):
                    traverse_no_checking(node1.less, node2.less)
                    traverse_no_checking(node1.less, node2.greater)
                    traverse_no_checking(node1.greater, node2.greater)
                else:
                    traverse_no_checking(node1.less, node2)
                    traverse_no_checking(node1.greater, node2)

        traverse_checking(self.tree, Rectangle(self.maxes, self.mins),
                          self.tree, Rectangle(self.maxes, self.mins))
        return results

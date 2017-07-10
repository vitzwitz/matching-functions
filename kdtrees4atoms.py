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
import scipy

__all__ = ['indexHelper', 'minmaxBC', 'nonzeroBC', 'returnMatches', 'allBC', 'maximumBC',
           'defyingDimensions', 'distance_matrix', 'Rectangle', 'KDTree4Atoms']

def indexHelper(i, atom):

    if i==0: return atom.x
    elif i==1: return atom.y
    elif i==2: return atom.z
    else: raise Warning

def minmaxBC(atoms, d=""):
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
        if comp == "<":
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
        elif comp == "==":
            if indexHelper(d, atom.position) != compVal:
                return False
        else:
            raise Warning

    return True

def maximumBC(pt1, pt2):
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

def isQualified(a, dist="", distance_upper_bound="", orEqual="", atomName="", res=""):
    if not isinstance(a, cl.Atom):
        if len(a) > 1:
            return qualifyingHelper(a, dist, distance_upper_bound, orEqual, atomName, res)
        elif len(a) == 1:
            a = a[0]
            if dist != "":
                dist = dist[0]
            return isQualified(a, dist, distance_upper_bound, orEqual, atomName, res)
        else:
            raise Warning
    else:
        # print("res", res, a.resName.strip())
        # print("atomName", atomName, a.name.strip())
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
        return f.euclideanDistance(zero, np.maximum(0,np.maximum(self.mins-other.maxes,other.mins-self.maxes)))

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
            raise ValueError("leafsize must be at least 1")
        self.mins, self.maxes = minmaxBC(atoms)
        print("mins:", self.mins)
        print("maxes:", self.maxes)
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
        def __init__(self, idx):
            self.idx = np.asarray(idx)
            self.children = len(idx)

    class innernode(node):
        def __init__(self, split_dim, split, less, greater):
            self.split_dim = split_dim
            self.split = split
            self.less = less
            self.greater = greater
            self.children = less.children+greater.children

    def __construct(self, idx, maxes, mins):
        if len(idx) <= self.leafsize:
            return KDTree4Atoms.leafnode(idx)
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
                return KDTree4Atoms.leafnode(idx)

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

    def __query(self, x, res, atomName, k=1, eps=0, distance_upper_bound=np.inf):
        if isinstance(x, cl.Atom):
            side_distances = np.maximum(0, np.maximum(defyingDimensions("-", x.position, self.maxes),
                                                      defyingDimensions("-", self.mins, x.position, True)))
        else:
            side_distances = np.maximum(0,np.maximum(defyingDimensions("-", x, self.maxes),defyingDimensions("-", self.mins, x, True)))
        min_distance = np.amax(side_distances)

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
        neighbors = []

        if eps == 0:
            epsfac = 1
        else:
            epsfac = 1/(1+eps)**2

        if distance_upper_bound != np.inf:
            distance_upper_bound = distance_upper_bound**2

        while q:
            min_distance, side_distances, node = heappop(q)
            if isinstance(node, KDTree4Atoms.leafnode):
                # brute-force
                data = returnMatches(self.data, node.idx)
                ds = []
                if not isinstance(x, cl.Atom):
                    " Check "
                    print("More than one atom object in __query")

                for atom in data:
                    ds.append(f.euclideanDistance(atom.position, x.position))
                ds = np.asarray(ds)
                for i in range(len(ds)):
                    if isQualified(self.data[node.idx[i]], ds[i], distance_upper_bound, atomName, res) == True:
                        if len(neighbors) == k:
                            heappop(neighbors)
                        heappush(neighbors, (ds[i], node.idx[i]))
                        if len(neighbors) == k:
                            distance_upper_bound = neighbors[0][0]
            else:
                # we don't push cells that are too far onto the queue at all,
                # but since the distance_upper_bound decreases, we might get
                # here even if the cell's too far
                if min_distance > distance_upper_bound*epsfac:
                    # since this is the nearest cell, we're done, bail out
                    break
                # compute minimum distances to the children and push them on
                if x[node.split_dim] < node.split:
                    " Check "
                    near, far = node.less, node.greater
                else:
                    near, far = node.greater, node.less

                # near child is at the same distance as the current node
                heappush(q,(min_distance, side_distances, near))

                # far child is further by an amount depending only
                # on the split value
                sd = list(side_distances)
                """
                Check
                """
                sd[node.split_dim] = f.euclideanDistance(node.split, x[node.split_dim].position)
                min_distance -= side_distances[node.split_dim] + sd[node.split_dim]

                # far child might be too far, if so, don't bother pushing it
                if min_distance <= distance_upper_bound*epsfac:
                    heappush(q,(min_distance, tuple(sd), far))

        return sorted(neighbors)

    def query(self, x, res="", atomName="", k=1, eps=0, distance_upper_bound=np.inf):
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
                hits = self.__query(x[c].ravel(), res, atomName, k=k, eps=eps, distance_upper_bound=distance_upper_bound)
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

        else:
            hits = self.__query(x, res, atomName, k=k, eps=eps, distance_upper_bound=distance_upper_bound)
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
                return atms#, dd, ii
            else:
                raise ValueError("Requested %s nearest neighbors; acceptable numbers are integers greater than or equal to one, or None")

    def __query_ball_point(self, x, r, res, atomName, eps=0):
        R = Rectangle(self.maxes, self.mins)
        def traverse_checking(node, rect):
            if rect.min_distance_point(x) > r / (1. + eps):
                return []
            elif rect.max_distance_point(x) < r * (1. + eps):
                return traverse_no_checking(node)
            elif isinstance(node, KDTree4Atoms.leafnode):

                d = self.data[node.idx]
                qualified = isQualified(d,f.euclideanDistance(d, x.position), r, "=", res, atomName)
                if isinstance(qualified, bool):
                    qualified = np.asarray([qualified])
                if len(qualified) != len(d):
                    raise Warning
                indices = []
                for ind in node.idx[qualified].tolist():
                    indices.append(int(ind))
                return indices
            else:
                less, greater = rect.split(node.split_dim, node.split)
                return traverse_checking(node.less, less) + \
                       traverse_checking(node.greater, greater)

        def traverse_no_checking(node):
            if isinstance(node, KDTree4Atoms.leafnode):
                d = self.data[node.idx]
                qualified = isQualified(d, res=res, atomName=atomName)
                if isinstance(qualified, bool):
                    qualified = np.asarray([qualified])
                if len(qualified) != len(d):
                    raise Warning
                indices = []
                for ind in node.idx[qualified].tolist():
                    indices.append(int(ind))
                return indices
            else:
                return traverse_no_checking(node.less) + \
                       traverse_no_checking(node.greater)
        return traverse_checking(self.tree, R)

    def query_ball_point(self, x, r, res="", atomName="", eps=0):
        """Find all points within distance r of point(s) x.

        Parameters
        ----------
        x : array_like, shape tuple + (self.m,)
            The point or points to search for neighbors of.
        r : positive float
            The radius of points to return.
        eps : nonnegative float, optional
            Approximate search. Branches of the tree are not explored if their
            nearest points are further than ``r / (1 + eps)``, and branches are
            added in bulk if their furthest points are nearer than
            ``r * (1 + eps)``.

        Returns
        -------
        results : list or array of lists
            If `x` is a single point, returns a list of the indices of the
            neighbors of `x`. If `x` is an array of points, returns an object
            array of shape tuple containing lists of neighbors.

        Notes
        -----
        If you have many points whose neighbors you want to find, you may save
        substantial amounts of time by putting them in a KDTree and using
        query_ball_tree.

        # Examples
        # --------
        # >>> from scipy import spatial
        # >>> x, y = np.mgrid[0:4, 0:4]
        # >>> points = zip(x.ravel(), y.ravel())
        # >>> tree = spatial.KDTree(points)
        # >>> tree.query_ball_point([2, 0], 1)
        # [4, 8, 9, 12]
        Editted:
        x : specific desired atom(s)
         ** Temp : by name, residue
        """


        # if isinstance(x,list):
        #     if len(x[0]) == 1:
        #         x = "newFunction"
        #     else:
        #         numAtoms = len(x[0])
        #         x = np.empty(numAtoms, dtype=np.object)
        #         for ob in np.ndindex(numAtoms):
        #             x[ob] = "newFunction"
        try:
            product = len(x[0].position)
        except:
            product = len(x.position)

        if product != self.m:
            raise ValueError("Searching for a %d-dimensional point in a "
                             "%d-dimensional KDTree" % (self.m, product))
        if isinstance(x, cl.Atom):
            return self.__query_ball_point(x, r, res, atomName, eps)
        else:
            x = np.asarray(x)
            retshape = x.shape[:-1]
            result = np.empty(retshape, dtype=np.object)
            for c in np.ndindex(retshape):
                result[c] = self.__query_ball_point(x[c], r, res, atomName, eps=eps)
            return result


    def query_ball_tree(self, other, r, res="", atomName="", eps=0):
        """Find all pairs of points whose distance is at most r

        Parameters
        ----------
        other : KDTree instance
            The tree containing points to search against.
        r : float
            The maximum distance, has to be positive.
        eps : float, optional
            Approximate search.  Branches of the tree are not explored
            if their nearest points are further than ``r/(1+eps)``, and
            branches are added in bulk if their furthest points are nearer
            than ``r * (1+eps)``.  `eps` has to be non-negative.

        Returns
        -------
        results : list of lists
            For each element ``self.data[i]`` of this tree, ``results[i]`` is a
            list of the indices of its neighbors in ``other.data``.

        """

        results = [[] for i in range(self.n)]

        def traverse_checking(node1, rect1, node2, rect2):
            if rect1.min_distance_rectangle(rect2) > r/(1.+eps):
                return
            elif rect1.max_distance_rectangle(rect2) < r*(1.+eps):
                traverse_no_checking(node1, node2)
            elif isinstance(node1, KDTree4Atoms.leafnode):
                if isinstance(node2, KDTree4Atoms.leafnode):
                    d = other.data[node2.idx]
                    for i in node1.idx:
                        qualified = isQualified(d, f.euclideanDistance(d, self.data[i].position), r, "=", res, atomName)
                        if isinstance(qualified, bool):
                            qualified = np.asarray([qualified])
                        if len(qualified) != len(d):
                            raise Warning
                        results[i] += node2.idx[qualified].tolist()
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
                traverse_checking(node1.greater,greater1,node2.less,less2)
                traverse_checking(node1.greater,greater1,node2.greater,greater2)

        def traverse_no_checking(node1, node2):
            if isinstance(node1, KDTree4Atoms.leafnode):
                if isinstance(node2, KDTree4Atoms.leafnode):
                    for i in node1.idx:
                        results[i] += node2.idx.tolist()
                else:
                    traverse_no_checking(node1, node2.less)
                    traverse_no_checking(node1, node2.greater)
            else:
                traverse_no_checking(node1.less, node2)
                traverse_no_checking(node1.greater, node2)

        traverse_checking(self.tree, Rectangle(self.maxes, self.mins),
                          other.tree, Rectangle(other.maxes, other.mins))
        return results

    def query_pairs(self, r, res1="", atomName1="", res2="", atomName2="", eps=0):
        """
        ** Motif connection **
        Find all pairs of points within a distance.

        Parameters
        ----------
        r : positive float
            The maximum distance.
        eps : float, optional
            Approximate search.  Branches of the tree are not explored
            if their nearest points are further than ``r/(1+eps)``, and
            branches are added in bulk if their furthest points are nearer
            than ``r * (1+eps)``.  `eps` has to be non-negative.

        Returns
        -------
        results : set
            Set of pairs ``(i,j)``, with ``i < j``, for which the corresponding
            positions are close.

        """
        results = set()

        def traverse_checking(node1, rect1, node2, rect2):
            if rect1.min_distance_rectangle(rect2) > r/(1.+eps):
                return
            elif rect1.max_distance_rectangle(rect2) < r*(1.+eps):
                traverse_no_checking(node1, node2)

            elif isinstance(node1, KDTree4Atoms.leafnode):
                if isinstance(node2, KDTree4Atoms.leafnode):
                    # Special care to avoid duplicate pairs
                    if id(node1) == id(node2):
                        d = self.data[node2.idx]
                        for i in node1.idx:
                            if self.data[i].name == atomName1 and self.data[i].resName == res1:
                                qualified = isQualified(d, f.euclideanDistance(d, self.data[i].position), r, "=", res2, atomName2)
                                if isinstance(qualified, bool):
                                    qualified = np.asarray([qualified])
                                if len(qualified) != len(d):
                                    raise Warning
                                for j in node2.idx[qualified]:
                                    # print(" ***************************************************** ")
                                    # print("Node2: atom2, res2", self.data[j].name, self.data[j].resName)
                                    results.add((i,j))
                    else:
                        " node1 != node2 "
                        d = self.data[node2.idx]
                        for i in node1.idx:
                            if self.data[i].name == atomName1 and self.data[i].resName == res1:
                                qualified = isQualified(d, f.euclideanDistance(d, self.data[i].position), r, "=", res2, atomName2)
                                if isinstance(qualified, bool):
                                    qualified = np.asarray([qualified])
                                if len(qualified) != len(d):
                                    raise Warning
                                for j in node2.idx[qualified]:
                                    # print(" ***************************************************** ")
                                    # print("Node2: atom2, res2", self.data[j].name, self.data[j].resName)
                                    results.add((i,j))
                            elif self.data[i].name == atomName2 and self.data[i].resName == res2:
                                qualified = isQualified(d, f.euclideanDistance(d, self.data[i].position), r, "=", res1, atomName1)
                                if isinstance(qualified, bool):
                                    qualified = np.asarray([qualified])
                                if len(qualified) != len(d):
                                    raise Warning
                                for j in node2.idx[qualified]:
                                    # print(" ***************************************************** ")
                                    # print("Node2: atom1, res1", self.data[j].name, self.data[j].resName)
                                    results.add((j,i))
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
            if isinstance(node1, KDTree4Atoms.leafnode):
                if isinstance(node2, KDTree4Atoms.leafnode):
                    # Special care to avoid duplicate pairs
                    if id(node1) == id(node2):
                        d = self.data[node2.idx]
                        for i in node1.idx:
                            if self.data[i].name == atomName1 and self.data[i].resName == res1:
                                qualified = isQualified(d, f.euclideanDistance(d, self.data[i].position), r, "=", res2, atomName2)
                                if isinstance(qualified, bool):
                                    qualified = np.asarray([qualified])
                                if len(qualified) != len(d):
                                    raise Warning
                                for j in node2.idx[qualified]:
                                    print(" ***************************************************** ")
                                    print("Node1: atom1, res1", self.data[i].name, self.data[i].resName)
                                    print("Node2: atom2, res2", self.data[j].name, self.data[j].resName)
                                    results.add((i,j))
                    else:
                        d = self.data[node2.idx]
                        for i in node1.idx:
                            if self.data[i].name == atomName1 and self.data[i].resName == res1:
                                qualified = isQualified(d, res=res2, atomName=atomName2)
                                if isinstance(qualified, bool):
                                    qualified = np.asarray([qualified])
                                if len(qualified) != len(d):
                                    raise Warning
                                for j in node2.idx[qualified]:
                                    print(" ***************************************************** ")
                                    print("Node1: atom1, res1", self.data[i].name, self.data[i].resName)
                                    print("Node2: atom2, res2", self.data[j].name, self.data[j].resName)
                                    results.add((i,j))
                            elif self.data[i].name == atomName2 and self.data[i].resName == res2:
                                qualified = isQualified(d, res=res1, atomName=atomName1)
                                if isinstance(qualified, bool):
                                    qualified = np.asarray([qualified])
                                if len(qualified) != len(d):
                                    raise Warning

                                for j in node2.idx[qualified]:
                                    print(" ***************************************************** ")
                                    print("Node1: atom2, res2", self.data[i].name, self.data[i].resName)
                                    print("Node2: atom1, res1", self.data[j].name, self.data[j].resName)
                                    results.add((j,i))
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

    def count_neighbors(self, other, r):
        """
        Count how many nearby pairs can be formed.

        Count the number of pairs (x1,x2) can be formed, with x1 drawn
        from self and x2 drawn from `other`, and where
        ``distance(x1, x2, p) <= r``.
        This is the "two-point correlation" described in Gray and Moore 2000,
        "N-body problems in statistical learning", and the code here is based
        on their algorithm.

        Parameters
        ----------
        other : KDTree instance
            The other tree to draw points from.
        r : float or one-dimensional array of floats
            The radius to produce a count for. Multiple radii are searched with
            a single tree traversal.

        Returns
        -------
        result : int or 1-D array of ints
            The number of pairs. Note that this is internally stored in a numpy
            int, and so may overflow if very large (2e9).

        """
        def traverse(node1, rect1, node2, rect2, idx):
            min_r = rect1.min_distance_rectangle(rect2)
            max_r = rect1.max_distance_rectangle(rect2)
            c_greater = r[idx] > max_r
            result[idx[c_greater]] += node1.children*node2.children
            idx = idx[(min_r <= r[idx]) & (r[idx] <= max_r)]
            if len(idx) == 0:
                return

            if isinstance(node1,KDTree4Atoms.leafnode):
                if isinstance(node2,KDTree4Atoms.leafnode):
                    ds = f.euclideanDistance(self.data[node1.idx][:,np.newaxis,:],
                                  other.data[node2.idx][np.newaxis,:,:]).ravel()
                    ds.sort()
                    result[idx] += np.searchsorted(ds,r[idx],side='right')
                else:
                    less, greater = rect2.split(node2.split_dim, node2.split)
                    traverse(node1, rect1, node2.less, less, idx)
                    traverse(node1, rect1, node2.greater, greater, idx)
            else:
                if isinstance(node2,KDTree4Atoms.leafnode):
                    less, greater = rect1.split(node1.split_dim, node1.split)
                    traverse(node1.less, less, node2, rect2, idx)
                    traverse(node1.greater, greater, node2, rect2, idx)
                else:
                    less1, greater1 = rect1.split(node1.split_dim, node1.split)
                    less2, greater2 = rect2.split(node2.split_dim, node2.split)
                    traverse(node1.less,less1,node2.less,less2,idx)
                    traverse(node1.less,less1,node2.greater,greater2,idx)
                    traverse(node1.greater,greater1,node2.less,less2,idx)
                    traverse(node1.greater,greater1,node2.greater,greater2,idx)

        R1 = Rectangle(self.maxes, self.mins)
        R2 = Rectangle(other.maxes, other.mins)
        if np.shape(r) == ():
            r = np.array([r])
            result = np.zeros(1,dtype=int)
            traverse(self.tree, R1, other.tree, R2, np.arange(1))
            return result[0]
        elif len(np.shape(r)) == 1:
            r = np.asarray(r)
            n, = r.shape
            result = np.zeros(n,dtype=int)
            traverse(self.tree, R1, other.tree, R2, np.arange(n))
            return result
        else:
            raise ValueError("r must be either a single value or a one-dimensional array of values")

    def sparse_distance_matrix(self, other, max_distance, p=2.):
        """
        Compute a sparse distance matrix

        Computes a distance matrix between two KDTrees, leaving as zero
        any distance greater than max_distance.

        Parameters
        ----------
        other : KDTree

        max_distance : positive float

        p : float, optional

        Returns
        -------
        result : dok_matrix
            Sparse matrix representing the results in "dictionary of keys" format.

        """
        """
        Import SciPy
        """
        result = scipy.sparse.dok_matrix((self.n,other.n))

        def traverse(node1, rect1, node2, rect2):
            if rect1.min_distance_rectangle(rect2, p) > max_distance:
                return
            elif isinstance(node1, KDTree4Atoms.leafnode):
                if isinstance(node2, KDTree4Atoms.leafnode):
                    for i in node1.idx:
                        for j in node2.idx:
                            d = f.euclideanDistance(self.data[i],other.data[j])
                            if d <= max_distance:
                                result[i,j] = d
                else:
                    less, greater = rect2.split(node2.split_dim, node2.split)
                    traverse(node1,rect1,node2.less,less)
                    traverse(node1,rect1,node2.greater,greater)
            elif isinstance(node2, KDTree4Atoms.leafnode):
                less, greater = rect1.split(node1.split_dim, node1.split)
                traverse(node1.less,less,node2,rect2)
                traverse(node1.greater,greater,node2,rect2)
            else:
                less1, greater1 = rect1.split(node1.split_dim, node1.split)
                less2, greater2 = rect2.split(node2.split_dim, node2.split)
                traverse(node1.less,less1,node2.less,less2)
                traverse(node1.less,less1,node2.greater,greater2)
                traverse(node1.greater,greater1,node2.less,less2)
                traverse(node1.greater,greater1,node2.greater,greater2)
        traverse(self.tree, Rectangle(self.maxes, self.mins),
                 other.tree, Rectangle(other.maxes, other.mins))

        return result


def distance_matrix(x,y,threshold=1000000):
    """
    Compute the distance matrix.

    Returns the matrix of all pair-wise distances.

    Parameters
    ----------
    x : (M, K) array_like
        TODO: description needed
    y : (N, K) array_like
        TODO: description needed
    p : float, 1 <= p <= infinity
        Which Minkowski p-norm to use.
    threshold : positive int
        If ``M * N * K`` > `threshold`, algorithm uses a Python loop instead
        of large temporary arrays.

    Returns
    -------
    result : (M, N) ndarray
        Distance matrix.

    Examples
    --------
    >>> distance_matrix([[0,0],[0,1]], [[1,0],[1,1]])
    array([[ 1.        ,  1.41421356],
           [ 1.41421356,  1.        ]])

    """

    x = np.asarray(x)
    m, k = x.shape
    y = np.asarray(y)
    n, kk = y.shape

    if k != kk:
        raise ValueError("x contains %d-dimensional vectors but y contains %d-dimensional vectors" % (k, kk))

    if m*n*k <= threshold:
        return f.euclideanDistance(x[:,np.newaxis,:],y[np.newaxis,:,:])
    else:
        result = np.empty((m,n),dtype=np.float)  # FIXME: figure out the best dtype
        if m < n:
            for i in range(m):
                result[i,:] = f.euclideanDistance(x[i],y)
        else:
            for j in range(n):
                result[:,j] = f.euclideanDistance(x,y[j])
        return result
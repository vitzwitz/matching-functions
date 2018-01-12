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

        if np.all(rect1.min_distance_rectangle(rect2) > np.asarray(r) / (1. + eps)):
            return
        elif np.all(rect1.max_distance_rectangle(rect2) < np.asarray(r) * (1. + eps)):
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
                                                                                 "Associated atom from atom 2: " +
                                                          atomName2[row])


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
                                                                                 "Associated atom from atom 2: " +
                                                          atomName2[row])

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
                                                raise Warning(
                                                    "traverse_checking (Case 2, part 1): Results is not a list")

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
                                                                                 "Associated atom from atom 2: " +
                                                          atomName2[row])



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
                                                raise Warning(
                                                    "traverse_checking (Case 3, part 1): Results is not a list")
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
                traverse_checking(node1, rect1, node2.less, less)
                traverse_checking(node1, rect1, node2.greater, greater)
        elif isinstance(node2, KDTree4Atoms.leafnode):
            less, greater = rect1.split(node1.split_dim, node1.split)
            traverse_checking(node1.less, less, node2, rect2)
            traverse_checking(node1.greater, greater, node2, rect2)
        else:
            less1, greater1 = rect1.split(node1.split_dim, node1.split)
            less2, greater2 = rect2.split(node2.split_dim, node2.split)
            traverse_checking(node1.less, less1, node2.less, less2)
            traverse_checking(node1.less, less1, node2.greater, greater2)

            # Avoid traversing (node1.less, node2.greater) and
            # (node1.greater, node2.less) (it's the same node pair twice
            # over, which is the source of the complication in the
            # original KDTree.query_pairs)
            if id(node1) != id(node2):
                traverse_checking(node1.greater, greater1, node2.less, less2)

            traverse_checking(node1.greater, greater1, node2.greater, greater2)

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
                                                                                 "Associated atom from atom 2: " +
                                                          atomName2[row])

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
                                                                                      "Associated atom from atom 2: " +
                                                          atomName2[row])

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
                                                                                 "Associated atom from atom 2: " +
                                                          atomName2[row])

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

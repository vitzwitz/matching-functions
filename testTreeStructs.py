
import numpy as np
from numpy import *
import decimal
import functions as f
from testing import *
import numpy



class Node(object):
    def __init__(self, value, idx=0, LEFT=None, RIGHT=None):
            self.data = value
            self.left = LEFT
            self.right = RIGHT




def testTrees():
    root = None
    for i in range(0,3):
        if root == None:
            root = Node(i)
        else:
            pass
testTrees()
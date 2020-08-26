class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

class BinarySearchTree:

    def __init__(self):
        self.root = None

    def minimum(self, x):
        while x.left != None:
            x = x.left
        return x




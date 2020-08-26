#!/usr/bin/python

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

"""
Pseudocode fo this function
1) Create an empty stack (called stack)
2) Push the current node to the stack S and set current = current.left 
3) If the current is Null and the stack is not empty
    a) pop item at the top of the stack
    b) print the popped item
    c) go to step 3
"""


def inorder_traversal(root):
    current = root
    stack = []
    # Reach the left most of the node that is provided
    while True:
        if current is not None:
            stack.append(current)
            current = current.left
        elif(stack):
            current = stack.pop()
            print(current.data)
            current = current.right
        else:
            break


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

inorder_traversal(root) # Runtime is O(n)
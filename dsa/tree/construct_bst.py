from dsa.tree.node import Node

"""
Construct BST
Design a Binary Search Tree class that supports following:
1.Insert a value
2.Remove a value
  method should remove first occurrence of a value
  a. leaf node
  b. node with one child
  c. node with two children
3.Find a value
  if value is found it should return node with value else return false
"""


def get_min(node):
    while node.left:
        node = node.left
    return node.value


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        node = Node(value)
        if not self.root:
            self.root = node
            return self
        tree = self.root
        while True:
            if value < tree.value:
                if not tree.left:
                    tree.left = node
                    return self
                tree = tree.left
            else:
                if not tree.right:
                    tree.right = node
                    return self
                tree = tree.right

    def find(self, value):
        if not self.root:
            return False
        tree = self.root
        while tree:
            if value < tree.value:
                tree = tree.left
            elif value > tree.value:
                tree = tree.right
            elif value == tree.value:
                return tree
        return False

    def remove(self, value, current=None, parent=None):
        if not self.root:
            return False
        if not current:
            current = self.root
        while current:
            if value < current.value:
                parent = current
                current = current.left
            elif value > current.value:
                parent = current
                current = current.right
            else:
                if current.left and current.right:
                    current.value = get_min(current.right)
                    self.remove(current.value, current.right, current)
                elif parent is None:
                    if current.left:
                        current.value = current.left.value
                        current.right = current.left.right
                        current.left = current.left.left
                    elif current.right:
                        current.value = current.right.value
                        current.right = current.right.right
                        current.left = current.right.left
                    else:
                        self.root = None
                elif current == parent.left:
                    parent.left = current.left if current.left else current.right
                elif current == parent.right:
                    parent.right = current.left if current.left else current.right
                break

        return self

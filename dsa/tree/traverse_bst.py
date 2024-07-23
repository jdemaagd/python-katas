"""
Traverse BST
Write 4 instance methods for a Binary Search Tree class to traverse BST:
1. Method 1 :
   traverse tree breadth first and return an array that contains all values of BST
2. Method 2 :
   traverse tree depth first (in-order) and return an array that contains all values of BST
3. Method 3 :
   traverse tree depth first (pre-order) and return an array that contains all values of BST
4. Method 4 :
   traverse tree depth first (post-order) and return an array that contains all values of BST
"""


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def bread_first(self):
        if not self.root:
            return []
        array = []
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            array.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return array

    def dfs_in_order(self):
        if not self.root:
            return []
        array = []
        current = self.root

        def trav(node):
            if node.left:
                trav(node.left)
            array.append(node.value)
            if node.right:
                trav(node.right)

        trav(current)
        return array

    def dfs_pre_order(self):
        if not self.root:
            return []
        array = []
        current = self.root

        def trav(node):
            array.append(node.value)
            if node.left:
                trav(node.left)
            if node.right:
                trav(node.right)

        trav(current)
        return array

    def dfs_post_order(self):
        if not self.root:
            return []
        array = []
        current = self.root

        def trav(node):
            if node.left:
                trav(node.left)
            if node.right:
                trav(node.right)
            array.append(node.value)

        trav(current)

        return array

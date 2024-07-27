from collections import deque
from dsa.tree.binary_tree import BinaryTree
from dsa.tree.print_tree import print_tree

"""
Invert Binary Tree
Given the root of a binary tree, invert the tree, and return its root.
Invert means swap every left node for its corresponding right node / get mirror image.
BFS: Iterative
while queue.length:
    dequeue
    swap left and right
    if left: enqueue left
    if right: enqueue right
Time Complexity: O(n)
Space Complexity: O(n)
DFS: Recursive
Base Case: if root is None, return
Recursive Case: swap left and right
Time Complexity: O(n)
Space Complexity: O(max depth) = O(height)
"""


def invert_iterative(root):
    if root is None:
        return

    queue = deque([root])

    while queue:
        current = queue.popleft()
        current.left, current.right = current.right, current.left
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return root


def invert_recursive(node):
    if node is None:
        return

    temp = node.left
    node.left = node.right
    node.right = temp

    invert_recursive(node.left)
    invert_recursive(node.right)

    return node


if __name__ == "__main__":
    tree = BinaryTree()
    tree.insert([4, 2, 7, 1, 3, 6, 9])
    print_tree(invert_iterative(tree.root))     # [4, 7, 2, 9, 6, 3, 1]
    print_tree(invert_recursive(tree.root))     # [4, 2, 7, 1, 3, 6, 9], works on inverted tree, so back to original

    print()
    tree2 = BinaryTree()
    tree2.insert([1, 2, 7, 4, 5, None, 7])
    print_tree(invert_iterative(tree2.root))    # [1, 7, 2, 7, None, 5, 4]
    print_tree(invert_recursive(tree2.root))    # [1, 2, 7, 4, 5, None, 7], works on inverted tree, so back to original

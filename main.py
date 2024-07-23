import sys
import os

from dsa.tree.construct_bst2 import build_tree
from dsa.tree.print_tree import print_tree
from dsa.tree.side_view import left_view, right_view
from dsa.tree.traverse_bst import BinarySearchTree
from dsa.tree.level_order_traversal import BinaryTree
from dsa.tree.node import Node

# get directory of current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# add dsa directory to system path
sys.path.append(os.path.join(current_dir, 'dsa'))

if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.root = Node(10)
    bst.root.left = Node(5)
    bst.root.right = Node(15)
    bst.root.left.left = Node(2)
    bst.root.left.right = Node(7)
    bst.root.right.right = Node(20)

    print("DFS In Order:", bst.dfs_in_order())  # [2, 5, 7, 10, 15, 20]
    print()

    print("Construct BST from Preorder and Inorder Traversal")
    preorder1 = [3, 9, 20, 15, 7]
    inorder1 = [9, 3, 15, 20, 7]
    tree1 = build_tree(None, preorder1, inorder1)
    print(print_tree(tree1))  # [3, 9, 20, None, None, 15, 7]

    preorder2 = [-1]
    inorder2 = [-1]
    tree2 = build_tree(None, preorder2, inorder2)
    print(print_tree(tree2))  # [-1]
    print()

    print("Construct BST from Postorder and Inorder Traversal")
    inorder1 = [9, 3, 15, 20, 7]
    postorder1 = [9, 15, 7, 20, 3]
    tree1 = build_tree(None, inorder1, postorder1)
    print(print_tree(tree1))  # Output: [3, 9, 20, None, None, 15, 7]

    inorder2 = [-1]
    postorder2 = [-1]
    tree2 = build_tree(None, inorder2, postorder2)
    print(print_tree(tree2))  # Output: [-1]
    print()

    print("Create Binary Tree & Insert Elements")
    tree = BinaryTree()
    tree.insert([7, 11, 1, None, 7, 2, 8, None, None, None, 3, None, None, 5, None])
    print(print_tree(tree.root))
    print()

    print("Side Views of Tree")
    tree = BinaryTree()
    tree.insert([7, 11, 1, None, 7, 2, 8, None, None, None, 3, None, None, 5, None])
    print(left_view(tree.root))

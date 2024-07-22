import sys
import os

from dsa.tree.node import Node
from dsa.tree.traverse_bst import BinarySearchTree

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the dsa directory to the system path
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

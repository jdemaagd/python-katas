from typing import List, Optional
from dsa.tree.node import Node
from dsa.tree.print_tree import print_tree

"""
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary
tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

Recall inorder: elements to left of root element are in left subtree
                and elements to right are in right subtree
Recall postorder: last element is always root of tree
"""


def build_tree(self, inorder: List[int], postorder: List[int]) -> Optional[Node]:
    inorder_map = {value: idx for idx, value in enumerate(inorder)}

    def array_to_tree(in_left, in_right, post_left, post_right):
        if in_left > in_right or post_left > post_right:
            return None

        root_val = postorder[post_right]
        root = Node(root_val)

        in_root_index = inorder_map[root_val]

        left_tree_size = in_root_index - in_left

        root.left = array_to_tree(in_left, in_root_index - 1, post_left, post_left + left_tree_size - 1)
        root.right = array_to_tree(in_root_index + 1, in_right, post_left + left_tree_size, post_right - 1)

        return root

    return array_to_tree(0, len(inorder) - 1, 0, len(postorder) - 1)


if __name__ == "__main__":
    print("Construct BST from Postorder and Inorder Traversal")
    inorder1 = [9, 3, 15, 20, 7]
    postorder1 = [9, 15, 7, 20, 3]
    tree1 = build_tree(None, inorder1, postorder1)
    print(print_tree(tree1))    # Output: [3, 9, 20, None, None, 15, 7]

    inorder2 = [-1]
    postorder2 = [-1]
    tree2 = build_tree(None, inorder2, postorder2)
    print(print_tree(tree2))    # Output: [-1]

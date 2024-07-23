from typing import List, Optional
from dsa.tree.node import Node

"""
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary
tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

Recall preorder: first element is always root of tree
Recall inorder: elements to left of root element are in left subtree
                and elements to right are in right subtree

Example 1: construct-example.png
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Example 2:
Input: preorder = [-1], inorder = [-1]
Output: [-1]

Constraints:
1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.
"""


def build_tree(self, preorder: List[int], inorder: List[int]) -> Optional[Node]:
    inorder_map = {value: idx for idx, value in enumerate(inorder)}

    def array_to_tree(pre_left, pre_right, in_left, in_right):
        if pre_left > pre_right or in_left > in_right:
            return None

        root_val = preorder[pre_left]
        root = Node(root_val)
        in_root_index = inorder_map[root_val]

        left_tree_size = in_root_index - in_left

        root.left = array_to_tree(pre_left + 1, pre_left + left_tree_size, in_left, in_root_index - 1)
        root.right = array_to_tree(pre_left + left_tree_size + 1, pre_right, in_root_index + 1, in_right)

        return root

    return array_to_tree(0, len(preorder) - 1, 0, len(inorder) - 1)


def build_tree2(self, preorder: List[int], inorder: List[int]) -> Optional[Node]:
    if not preorder or not inorder:
        return None

    # first element of preorder is root
    root_val = preorder[0]
    root = Node(root_val)

    root_index = inorder.index(root_val)

    left_inorder = inorder[:root_index]
    right_inorder = inorder[root_index + 1:]

    left_preorder = preorder[1:1 + len(left_inorder)]
    right_preorder = preorder[1 + len(left_inorder):]

    root.left = build_tree(left_preorder, left_inorder)
    root.right = build_tree(right_preorder, right_inorder)

    return root

"""
Iterative solution for Preorder Traversal of a Binary Tree
Given the root of a binary tree, return the preorder traversal of its nodes' values.
Recall: root, left, right
while stack is not empty:
    pop node from stack
    add node?.value to result array
    add right child node to stack
    add left child node to stack
Time Complexity: O(n), where n is number of nodes in tree
Space Complexity: O(h), where h is max height of tree
"""


def preorder_traversal(root):
    if not root:
        return []

    stack = [root]
    result = []

    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result

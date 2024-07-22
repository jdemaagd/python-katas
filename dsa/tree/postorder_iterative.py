"""
Iterative solution for Postorder Traversal of a Binary Tree
Given the root of a binary tree, return the postorder traversal of its nodes' values.
Recall: left, right, root
while stack:
    curr = 1
    visited = false
    if curr AND visited:
        append curr?.value to result array
    else:
        append curr to stack, True to visited
        append curr?.right to stack, False to visited
        append curr?.left to stack, False to visited
Time Complexity: O(n), where n is number of nodes in tree
Space Complexity: O(h), where h is max height of tree, height determines stack usage
"""


def postorder_traversal(root):
    if not root:
        return []

    stack = [(root, False)]
    result = []

    while stack:
        curr, visited = stack.pop()
        if visited:
            result.append(curr.val)
        else:
            stack.append((curr, True))
            if curr.right:
                stack.append((curr.right, False))
            if curr.left:
                stack.append((curr.left, False))

    return result

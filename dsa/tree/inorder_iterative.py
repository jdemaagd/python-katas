"""
Iterative solution for Inorder Traversal of a Binary Tree
Given the root of a binary tree, return the inorder traversal of its nodes' values.
Recall: left, root, right
1. keep going left as far as possible
2. come back to previous node before going right
3. after going right, go left again as much as possible
while curr points to a node OR stack is not empty: (we need to come back to root node)
    while curr points to a node:
        append curr to stack
        curr = curr?.left
    pop node from stack
    append node?.value to result array
    curr = curr?.right
Time Complexity: O(n), n is number of nodes in tree
Space Complexity: O(n), worst case when tree is skewed
"""


def inorder_traversal(root):
    if not root:
        return []

    stack = []
    result = []
    curr = root

    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        result.append(curr.val)
        curr = curr.right

    return result

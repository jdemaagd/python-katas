"""
Given the root of a binary tree and an integer targetSum,
return all root-to-leaf paths where the sum of the node values in the path equals targetSum.
Each path should be returned as a list of the node values, not node references.
A root-to-leaf path is a path starting from the root and ending at any leaf node.
A leaf is a node with no children.
NOTE: `return all root-to-leaf paths` is strong indication of backtracking
Time Complexity: O(n * h), where n is number of nodes and h is max height
    O(n^2) in worst case, where tree is skewed
Space Complexity: O(h), where h is the height of the tree
"""


def path_sum(root, target):
    res = []

    def helper(node, curr, rem):
        if node is None:
            return
        curr.append(node.val)   # choose
        if rem == node.val and node.left is None and node.right is None:
            res.append(curr[:])
        else:
            helper(node.left, curr, rem - node.val)
            helper(node.right, curr, rem - node.val)
        curr.pop()  # backtracking step

    helper(root, [], target)

    return res

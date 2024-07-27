from dsa.tree.binary_tree import BinaryTree

"""
Diameter of binary tree
Write function which takes in root of binary tree and returns length of diameter of tree.
Diameter of binary tree is length of longest path between any two nodes in tree.
It is not necessary for this path to pass through root of tree.
Length of path between two nodes is number of edges between them.
Recall: height of node is # edges on longest path between that node and leaf node.
Height of leaf node is 0.
Height of null node is -1.
Diameter at node is height(left) + height(right) + 1 + 1.
Height of node is max(height(left), height(right)) + 1.

max_diameter = 0
dfs {
    if null:
        return -1

    left_height = dfs(left)
    right_height = dfs(right)

    diameter = left_height + right_height + 2
    max_diameter = max(diameter, max_diameter)

    return max(left_height, right_height) + 1
}
return max_diameter

Time Complexity: O(n)
Space Complexity: O(n), worst case for unbalanced tree
"""


def diameter_of_tree(root):
    if not root:
        return 0

    max_diameter = 0

    def dfs(node):
        nonlocal max_diameter

        if not node:
            return -1

        leftHeight = dfs(node.left)
        rightHeight = dfs(node.right)

        diameter = leftHeight + rightHeight + 2
        max_diameter = max(max_diameter, diameter)

        return max(leftHeight, rightHeight) + 1

    dfs(root)

    return max_diameter


if __name__ == "__main__":
    tree = BinaryTree()
    tree.insert([1, 7, 8, None, None, 2, 5, 3, None, None, 6, 4, 10, None, None, None, None, None, 9])
    print(diameter_of_tree(tree.root))  # 6

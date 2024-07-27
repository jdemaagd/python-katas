from dsa.tree.binary_tree import BinaryTree

"""
Sum root to leaf numbers
You are given the root of a binary tree containing digits from 0 to 9 only.
Each root-to-leaf path in the tree represents a number.
    For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers.
Test cases are generated so that the answer will fit in a 32-bit integer.
A leaf node is a node with no children.

Time Complexity: O(n)
Space Complexity: O(n), worst case for unbalanced tree
"""


def sum_numbers(root) -> int:
    def dfs(node, current_number):
        if not node:
            return 0

        current_number = current_number * 10 + node.value

        if not node.left and not node.right:
            return current_number

        left_sum = dfs(node.left, current_number)
        right_sum = dfs(node.right, current_number)

        return left_sum + right_sum

    return dfs(root, 0)


if __name__ == "__main__":
    tree = BinaryTree()
    tree.insert([1, 2, 3])
    print(sum_numbers(tree.root))  # 25

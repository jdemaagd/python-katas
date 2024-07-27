from collections import defaultdict, deque
from dsa.tree.binary_tree import BinaryTree

"""
Vertical Order traversal of a Binary Tree
Given the root of a binary tree, calculate the vertical order traversal of the binary tree.
For each node at position (row, col), its left and right children will be at positions
(row + 1, col - 1) and (row + 1, col + 1) respectively.
The root of the tree is at (0, 0).
The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column
index starting from the leftmost column and ending on the rightmost column.
There may be multiple nodes in the same row and same column.
In such a case, sort these nodes by their values.
Return the vertical order traversal of the binary tree.

Time Complexity: O(n log n)
    bfs traversal -> O(n) 
    sorting columns -> O(n log n)
Space Complexity: O(n)
"""


def vertical_order_traversal(root):
    if not root:
        return []

    column_table = defaultdict(list)
    queue = deque([(root, 0, 0)])

    while queue:
        node, row, col = queue.popleft()

        if node is not None:
            column_table[col].append((row, node.value))
            queue.append((node.left, row + 1, col - 1))
            queue.append((node.right, row + 1, col + 1))

    sorted_columns = sorted(column_table.keys())
    result = []

    for col in sorted_columns:
        column_table[col].sort(key=lambda x: (x[0], x[1]))
        column_values = [val for row, val in column_table[col]]
        result.append(column_values)

    return result


if __name__ == "__main__":
    tree = BinaryTree()
    tree.insert([1, 2, 3, 4, 5, 6, 7])
    print(vertical_order_traversal(tree.root))  # [[4], [2], [1, 5, 6], [3], [7]]

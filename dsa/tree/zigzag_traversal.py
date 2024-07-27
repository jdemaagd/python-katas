from collections import deque
from dsa.tree.binary_tree import BinaryTree

"""
Given root of a binary tree, return the zigzag level order traversal of its nodes' values.
(i.e., from left to right, then right to left for the next level and alternate between).

Time Complexity: O(n)
Space Complexity: O(n)
"""


def zigzag_level_order(root):
    if not root:
        return []

    result = []
    queue = deque([root])
    left_to_right = True

    while queue:
        level_size = len(queue)
        level_nodes = deque()

        for _ in range(level_size):
            node = queue.popleft()

            if left_to_right:
                level_nodes.append(node.value)
            else:
                level_nodes.appendleft(node.value)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(list(level_nodes))
        left_to_right = not left_to_right

    return result


if __name__ == "__main__":
    tree = BinaryTree()
    tree.insert([1, 2, 3, 4, 5, None, 6])
    print(zigzag_level_order(tree.root))        # [[1], [3, 2], [4, 5, 6]]

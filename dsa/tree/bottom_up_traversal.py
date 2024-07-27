from collections import deque
from dsa.tree.binary_tree import BinaryTree

"""
Given root of binary tree, return bottom-up level order traversal of its nodes' values.
(i.e., from left to right, level by level from leaf to root).

Time complexity: O(n)
Space complexity: O(n)
"""


def level_order_bottom_up(root):
    if not root:
        return []

    result = deque()
    queue = deque([root])

    while queue:
        level_size = len(queue)
        level_nodes = []

        for _ in range(level_size):
            node = queue.popleft()
            level_nodes.append(node.value)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.appendleft(level_nodes)

    return list(result)


if __name__ == "__main__":
    tree = BinaryTree()
    tree.insert([1, 2, 3, 4, 5, None, 6])
    print(level_order_bottom_up(tree.root))     # [[4, 5, 6], [2, 3], [1]]

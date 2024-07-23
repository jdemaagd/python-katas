"""
Left/Right View of binary tree
1. Given the root of a binary tree, imagine yourself standing on the right side of it,
   return the values of the nodes you can see ordered from top to bottom.
2. Given the root of a binary tree, imagine yourself standing on the left side of it,
   return the values of the nodes you can see ordered from top to bottom.

Time Complexity: O(n)
Space Complexity: O(n/2) = O(n)
"""


def right_view(root):
    if root is None:
        return []
    right = []
    queue = [root]
    while queue:
        length = len(queue)
        count = 0
        while count < length:
            count += 1
            current = queue.pop(0)
            if count == length:
                right.append(current.value)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
    return right


def left_view(root):
    if root is None:
        return []

    left = []
    queue = [root]

    while queue:
        length = len(queue)
        count = 0
        while count < length:
            count += 1
            current = queue.pop(0)
            if count == 1:
                left.append(current.value)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
    return left

from collections import deque

"""
Level Order Traversal
Write a function that takes root of a binary tree, and returns level order traversal of its nodes'
values. (i.e., from left to right, level by level). Initially write an instance method for BST class
to insert the values given as an array into the Binary tree (from left to right, level by level).
Each value in the array which is not null is to be made a node and added to the tree.
(See examples below). Then write the function mentioned first.

Pseudocode:
while queue is not empty:
    dequeue
    if not left:
        if value not null:
            insert
            i++
    if left:
        enqueue
    if not right:
        if value not null:
            insert
            i++
    if right:
        enqueue

Time Complexity: O(n)
Space Complexity: O(n)
"""


def level_order_traversal(root):
    if root is None:  # This operation is O(1)
        return []

    output = []
    queue = deque([root])  # Creating a queue is O(1)
    while queue:  # The outer while loop will run for n iterations (n is the total number of nodes in the tree)
        length = len(queue)  # Getting the length of the queue is O(1)
        count = 0
        curr_level_values = []
        while count < length:  # This inner while loop will run for 'length' iterations
            curr = queue.popleft()  # Removing an element from the deque is O(1)
            curr_level_values.append(curr.value)  # Appending an element is O(1)
            if curr.left:
                queue.append(curr.left)  # Appending an element to deque is O(1)
            if curr.right:
                queue.append(curr.right)  # Appending an element to deque is O(1)
            count += 1
        output.append(curr_level_values)  # Appending a list of length 'length' is O(length)

    return output

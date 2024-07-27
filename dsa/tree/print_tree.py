def print_tree(node):
    """Helper function to print the tree in level order."""
    result = []

    if not node:
        print(result)

    queue = [node]

    while queue:
        current = queue.pop(0)
        if current:
            result.append(current.value)
            queue.append(current.left)
            queue.append(current.right)
        else:
            result.append(None)

    while result and result[-1] is None:
        result.pop()

    print(result)

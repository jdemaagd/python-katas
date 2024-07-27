from dsa.tree.node import Node
from dsa.tree.print_tree import print_tree


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, array):
        if len(array) == 0:
            return

        i = 0

        if self.root is None:
            if array[0] is None:
                return
            else:
                node = Node(array[0])
                self.root = node
                i += 1
                if i == len(array):
                    return self

        queue = [self.root]
        while queue:
            current = queue.pop(0)

            if current.left is None:
                if array[i] is not None:
                    node = Node(array[i])
                    current.left = node
                i += 1
                if i == len(array):
                    return self
            if current.left is not None:
                queue.append(current.left)

            if current.right is None:
                if array[i] is not None:
                    node = Node(array[i])
                    current.right = node
                i += 1
                if i == len(array):
                    return self
            if current.right is not None:
                queue.append(current.right)


if __name__ == "__main__":
    print("Create Binary Tree & Insert Elements")
    tree = BinaryTree()
    tree.insert([7, 11, 1, None, 7, 2, 8, None, None, None, 3, None, None, 5, None])
    print(print_tree(tree.root))

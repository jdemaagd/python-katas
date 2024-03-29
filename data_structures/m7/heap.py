class MinHeap:
    def __init__(self):
        self.heap = [0]     # NOTE: dummy first element (to maintain easy parent-child index relationship)
        self.size = 0

    # NOTE: heapify when heap property is violated (root is min value)
    def arrange(self, k):
        while k // 2 > 0:
            if self.heap[k] < self.heap[k // 2]:    # NOTE: compare parent and child node values
                self.heap[k], self.heap[k // 2] = self.heap[k // 2], self.heap[k]   # NOTE: swap parent and child
            k //= 2    # NOTE: move up the tree

    def insert(self, item):
        self.heap.append(item)
        self.size += 1
        self.arrange(self.size)

    # NOTE: heapify (percolate down)
    def sink(self, k):
        while k * 2 <= self.size:
            mc = self.min_child(k)              # NOTE: find index of min child
            if self.heap[k] > self.heap[mc]:    # NOTE: compare parent and min child
                self.heap[k], self.heap[mc] = self.heap[mc], self.heap[k]       # NOTE: swap parent and min child
            k = mc      # NOTE: move down the tree

    def min_child(self, k):
        if k * 2 + 1 > self.size:       # NOTE: check if past end of list
            return k * 2                # NOTE: index of left child
        elif self.heap[k * 2] < self.heap[k * 2 + 1]:
            return k * 2                # NOTE: index of left child
        else:
            return k * 2 + 1            # NOTE: index of right child

    def delete_at_root(self):
        item = self.heap[1]                     # NOTE: copy of root
        self.heap[1] = self.heap[self.size]     # NOTE: swap root with last element
        self.size -= 1
        self.heap.pop()                         # NOTE: remove last element (was root)
        self.sink(1)
        return item

    def delete_at_location(self, location):
        item = self.heap[location]                      # NOTE: copy of node to be deleted
        self.heap[location] = self.heap[self.size]      # NOTE: swap node to be deleted with last element
        self.size -= 1
        self.heap.pop()                                 # NOTE: remove last element (was node to be deleted)
        self.sink(location)
        return item


h = MinHeap()
for i in (4, 8, 7, 2, 9, 10, 5, 1, 3, 6):
    h.insert(i)
print(h.heap)

n = h.delete_at_root()
print(n)
print(h.heap)

h = MinHeap()
for i in (4, 8, 7, 2, 9, 10, 5, 1, 3, 6):
    h.insert(i)
print(h.heap)

n = h.delete_at_location(2)
print(n)
print(h.heap)

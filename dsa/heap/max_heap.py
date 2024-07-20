"""
Max Heap Construction
Write a max Heap Class that supports the following:
    - Building a Max heap from an input array
    - Inserting integers in the Heap
    - Removing the Heap’s maximum / root value
    - Peeking at the Heap’s maximum / root value
The Heap is to be represented in the form of an array.
"""


def bubble_down(array, idx):
    length = len(array)
    current = array[idx]
    while True:
        left_child_idx = 2 * idx + 1
        right_child_idx = 2 * idx + 2
        largest = None

        if left_child_idx < length:
            left_child = array[left_child_idx]
            if left_child > current:
                largest = left_child_idx

        if right_child_idx < length:
            right_child = array[right_child_idx]
            if (largest is None and right_child > current) or (
                    largest is not None and right_child > array[largest]):
                largest = right_child_idx

        if largest is None:
            break
        else:
            array[idx], array[largest] = array[largest], array[idx]
            idx = largest


class MaxBinaryHeap:
    def __init__(self):
        self.heap = []

    def build_heap(self, array):
        length = len(array)
        last_parent_index = length // 2 - 1
        for i in range(last_parent_index, -1, -1):
            bubble_down(array, i)
        self.heap = array
        return self

    def extract_max(self):
        max_value = self.heap[0]
        last = self.heap.pop()
        if len(self.heap) > 0:
            self.heap[0] = last
            bubble_down(self.heap, 0)
        return max_value

    def insert(self, value):
        self.heap.append(value)
        self.bubble_up()
        return self

    def peek(self):
        return self.heap[0]

    def print_heap(self):
        print(self.heap)

    def bubble_up(self):
        idx = len(self.heap) - 1
        value = self.heap[idx]
        while idx > 0:
            parent_idx = (idx - 1) // 2
            parent_value = self.heap[parent_idx]
            if value <= parent_value:
                break
            self.heap[parent_idx], self.heap[idx] = self.heap[idx], self.heap[parent_idx]
            idx = parent_idx


heap = MaxBinaryHeap()
max_heap = heap.build_heap([4, 7, 3, 0, 9, 3, 2, 6])
heap.print_heap()           # [9, 7, 3, 6, 4, 3, 2, 0]
print(heap.peek())

heap.extract_max()
heap.print_heap()
print(heap.peek())

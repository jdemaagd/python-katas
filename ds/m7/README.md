# Heaps & Priority Queues

## Heap

- Data structure where each data elements satisfies a heap property
- Max Heap
    - parent node value must be greater than or equal to its children values
    - root node must have the largest value
- Min Heap
    - parent node value must be less than or equal to its children values
    - root node must have the smallest value
- Has several applications and uses in implementing heap sort algorithms and priority queues

### Binary Heap

- Given a complete binary tree with n nodes, its min height will be log base 2 n
- Then derive that a relationship between parent and child nodes is in index values
- Children of any node at the n index can be retrieved easily
    - left child will be located at 2n
    - right child will be located at 2n + 1
- Let's say we have a list of elements { A, B, C, D, E }
- If we store any element at an index of i
    - then its parent can be stored at index i/2
    - if the index of the node D is 4,
    - then its parent would be at 4/2 = 2, index 2
- The index of root has to be starting from 1 in the array (constraint)
    - need one dummy element at index 0 in array

## Heap Sort

- Step 1: Create a min-heap using all the given data elements.
- Step 2: Read and delete the root element, which is the minimum value.
    - After that, copy last element of tree to new root, and further reorganize tree to maintain heap property.
- Step 3: Now, we repeat step 2 until we get all the elements.
- Step 4: Finally, we get the sorted list of elements.

## Priority Queue

- Similar to a queue in which data is retrieved based on the First In, First Out (FIFO) policy
- But a priority is attached with the data
- Data is retrieved based on priority associated with data elements
- Used in many applications such as CPU scheduling, networking, Dijkstra's shortest-path, A* search, and Huffman codes
  for data compression

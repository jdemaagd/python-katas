# Exercises

## Question 1

```
What will be the time complexity for deleting an arbitrary element from the min-heap?

Solution
To delete any element from the heap, we first have to search the element that is to be deleted, 
and then we delete the element.
Total time complexity = time searching for element + deleting element
    = O(n) + O(log n)
    = O(n)
```

## Question 2

```
What will be the time complexity for finding the kth smallest element from the min-heap?

Solution
The kth element can be found from min-heap by performing delete operations k times. 
For each delete operation, time complexity is O(log n). 
So, total time complexity for finding kth smallest element will be O(k log n).
```

## Question 3

```
What will be the time complexity to make a max-heap that combines two max-heap each of size n?

Solution
O(n).
Since time complexity of creating a heap from n elements is O(n), 
creating a heap of 2n elements will also be O(n).
```

## Question 4

```
What will be the worst-case time complexity for ascertaining the smallest element from a binary
max-heap and binary min-heap?

Solution
In a max-heap, the smallest element will always be present at a leaf node. 
So, in order to find out the smallest element, we have to search all the leaf nodes. 
So, the worst-case complexity will be O(n).
The worst-case time complexity to find out the smallest element in the min-heap will be O(1)
since it will always be present at the root node.
```

## Question 5

```
The level order traversal of max-heap is 12, 9, 7, 4, and 2. 
After inserting new elements 1 and 8, 
what will be the final max-heap and the level order traversal of the final max-heap?

Solution
The level order traversal of the final max-heap will be 12, 9, 8, 4, 2, 1, 7
```

## Question 6

```
Which of the following is a binary max-heap?

Solution
Option b
A binary max-heap should be a complete binary tree with all levels filled, except last level. 
The value of the parent should be greater or equal to the values of its children.
Option A is not correct because it is not a complete binary tree. 
Options C and D are not correct because they are not fulfilling the heap property. 
Option B is correct because it is complete and fulfills the heap property.
```

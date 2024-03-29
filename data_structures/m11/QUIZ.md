# Exercises

## Question 1

```
If an array arr = {55, 42, 4, 31} is given and bubble sort is used to sort the array elements, 
then how many iterations will be required to sort the array?
a. 3
b. 2
c. 1
d. 0

Solution: a
To sort n elements, bubble sort algorithm requires (n - 1) iterations (passes),
where n is the number of elements in the given array
Here, n = 4, so (4 - 1) = 3 iterations
```

## Question 2

```
What is the worst-case complexity of bubble sort?
a. O(n log n)
b. O(log n)
c. O(n)
d. O(n^2)

Solution: d
```

## Question 3

```
Apply quicksort to the sequence (56, 89, 23, 99, 45, 12, 66, 78, 34). 
What is the sequence after the first phase, and what pivot is the first element?
a. 45, 23, 12, 34, 56, 99, 66, 78, 89
b. 34, 12, 23, 45, 56, 99, 66, 78, 89
c. 12, 45, 23, 34, 56, 89, 78, 66, 99
d. 34, 12, 23, 45, 99, 66, 89, 78, 56

Solution: b
```

## Question 4

```
Quicksort is a ___________
a. Greedy algorithm
b. Divide and conquer algorithm
c. Dynamic programming algorithm
d. Backtracking algorithm

Solution: b
```

## Question 5

```
Consider a situation where a swap operation is very costly. 
Which of the following sorting algorithms should be used 
so that the number of swap operations is minimized?
a. Heap sort
b. Selection sort
c. Insertion sort
d. Merge sort

Solution: b
In selection sort algorithm, we identify largest element, and then swap it
with last element so that in each iteration, only one swap is required
For n elements, the total (n-1) swaps will be required, 
which is the lowest in comparison to all other algorithms
```

## Question 6

```
If the input array A = {15, 9, 33, 35, 100, 95, 13, 11, 2, 13} is given, 
using selection sort, what would the order of the array be after the fifth swap? 
(Note: it counts regardless of whether they exchange places or remain in the same position)
a. 2, 9, 11, 13, 13, 95, 35, 33, 15, 100
b. 2, 9, 11, 13, 13, 15, 35, 33, 95, 100
c. 35, 100, 95, 2, 9, 11, 13, 33, 15, 13
d. 11, 13, 9, 2, 100, 95, 35, 33, 13, 13

Solution: a
```

## Question 7

```
What will be the number of iterations to sort the elements {44, 21, 61, 6, 13, 1}
using insertion sort?
a. 6
b. 5
c. 7
d. 1

Solution: a
Suppose there are n keys in an input list, 
then it requires n iterations to sort the entire list using insertion sort.
```

## Question 8

```
How will the array elements A = [35, 7, 64, 52, 32, 22] look after the second iteration,
if the elements are sorted using insertion sort?
a. 7, 22, 32, 35, 52, 64
b. 7, 32, 35, 52, 64, 22
c. 7, 35, 52, 64, 32, 22
d. 7, 35, 64, 52, 32, 22

Solution: d
```

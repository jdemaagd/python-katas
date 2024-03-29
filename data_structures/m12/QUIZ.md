# Exercises

## Question 1

```
What will be the output if the quickselect algorithm is applied to the given array
arr = [3, 1, 10, 4, 6, 5] with k given as 2?

Solution
find the median of medians: 4 (index = 3)
swap the pivot element with the first element: [4, 1, 3, 10, 6, 5]
move the pivot element to its correct position: [1, 3, 4, 10, 6, 5]
split index equal to 2 but the value of k is also equal to 2, 
hence the value at index 2 will be our output, hence the output will be 4
```

## Question 2

```
Can quickselect find the smallest element in an array with duplicate values?

Solution
Yes, it works. By the end of every iteration, 
we have all elements less than the current pivot stored to the left of the pivot
Let's consider when all elements are the same. 
In this case, every iteration ends up putting a pivot element to left of array
And the next iteration will continue with one element shorter in the array
```

## Question 3

```
What is the difference between the quicksort algorithm and the quickselect algorithm?

Solution
quickselect
we do not sort the array
specifically for finding kth smallest element in array
repeatedly divides array into two sections based on value of pivot 
pivot element will be placed such that 
all the elements to its left are smaller than the pivot element
and all the elements to the right are larger than the pivot element
we can select any one of the segments of the array based on the target value. 
the size of the operable range of our array keeps on reducing
reduces complexity from O(n log 2(n)) to O(n)
```

## Question 4

```
What is the main difference between the deterministic selection algorithm 
and the quickselect algorithm?

Solution
quickselect algorithm
we find the kth smallest element in an unordered list based on
picking up the pivot element randomly
deterministic selection algorithm, 
also used for finding kth smallest element from an unordered list
but in this algorithm, we choose a pivot element by using median of medians
instead of taking any random pivot element
```

## Question 5

```
What triggers the worst-case behavior of the selection algorithm?

Solution
Continuously picking largest or smallest element on each iteration 
triggers worst-case behavior of selection algorithm
```

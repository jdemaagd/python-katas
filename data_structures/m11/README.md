# Sorting

## Bubble Sort (Brute Force)

- Perform comparison between adjacent items in list and swap if they are not in correct order
- Repeat process for n - 1 times for a list of n items
- In each iteration, the largest element of list is moved to end of list (bubbles up)
- Time complexity: O(n^2)

## Insertion Sort (Brute Force)

- Maintain two sub-lists, one that is sorted and one that is not sorted
- Items are added one by one from the unsorted sublist to the sorted sublist
- In each iteration, item from unordered sublist is inserted at correct position in sorted sublist
- Time complexity: O(n^2)

## Selection Sort (Brute Force)

- Find the smallest item in list and interchange it with data stored at first position in list
- Next, find the second smallest item and interchanged with second position in list
- Repeat process for n - 1 times for a list of n items
- Time complexity: O(n^2)

## Quick Sort (Divide and Conquer)

- Idea is similar to merge sort
- But we use pivot to partition list into two sub-lists
    - NOTE: random pivot recommended for best time complexity
- Time complexity: O(n log n), when using random pivot
- Worst case time complexity: O(n^2), chance when not considering pivot

## Timsort

- Default standard sorting algorithm in all Python versions >=2.3
- Based on combination of merge and insertion sort algorithms
    - insertion sort works best when array is sorted partially and its size is small
    - merge sort algorithm works fast when we have to combine small, sorted lists
    - uses insertion sort to sort small blocks (chunks) of data elements
    - then uses merge sort algorithm to merge all sorted chunks
- Takes advantage of already-sorted data elements known as `natural runs`, which occur very
  frequently in real-world data

## Algorithm (Timsort)

- Divide given array of data elements into a number of blocks which are also known as a run
- Typically, use 32 or 64 as size of run as it is suitable for Timsort
    - but can use any other size that can be computed from length of given array
    - minrun is minimum length of each run
    - size of minrun can be computed by following given principles
        - minrun size should not be too long as we use insertion sort algorithm to sort these small
          blocks, which performs well for short lists of elements
        - length of run should not be very short; in that case, it will result in greater number of
          runs, which will make merging algorithm slow
        - since merge sort works best when we have number of runs as a power of 2, it would be good
          if number of runs that compute as N/minrun are a power of 2
- For example, if we take a run size of 32, then the number of runs will be (n / 32)
    - if this is a power of 2, then merge process will be very efficient
- Sort each of the runs one by one using the insertion sort algorithm
- Merge all the sorted runs one by one using the merge method of the merge sort algorithm
- After each iteration, we double the size of the merged subarray

## Time Complexity

|   Algorithm    | worst-case | average-case | best-case  |
|:--------------:|:----------:|:------------:|:----------:|
|  Bubble sort   |   O(n^2)   |    O(n^2)    |    O(n)    |
| Insertion sort |   O(n^2)   |    O(n^2)    |    O(n)    |
| Selection sort |   O(n^2)   |    O(n^2)    |   O(n^2)   |
|   QuickSort    |   O(n^2)   |  O(n log n)  | O(n log n) |
|    Timsort     | O(n log n) |  O(n log n)  |    O(n)    |

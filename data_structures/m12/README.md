# Selection Algorithms

## Selection by Sorting

## Randomized Selection (QuickSelect)

- Find kth smallest element in an unordered list of items
- Based on the quicksort algorithm
- Recursively call function only for sublist that has kth smallest element
- Compare index of pivot point with k value to obtain kth smallest element from given unordered list
    - if index of pivot point is smaller than k, then we are sure that kth smallest value will be
      present on right-hand sublist of pivot point, so recursively call quickselect function for
      right sublist
    - if index of pivot point is greater than k, then it is obvious that kth smallest element will
      be present on left-hand side of pivot point, so recursively call quickselect function for left
      sublist
    - if index of pivot point is equal to k, then it means that we have found kth smallest value,
      and return it
- Time complexity -> O(n)

## Deterministic Selection

- Split list of unordered items into groups of five elements each (number 5 is arbitrary)
- Sort these groups (i.e. insertion sort) and find median of all these groups
- Recursively, find median of medians obtained from these groups; let's say that is point `p`
- Using this point `p`, as pivot element, recursively call partition algorithm similar to
  quickselect to find out the kth smallest element

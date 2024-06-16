# Arrays

## Operations

- Access: Space & Time Complexity --> O(1)
- Set: Space & Time Complexity --> O(1)
- Traverse/Search: Space --> O(1), Time Complexity --> O(n)
- Copy: Space & Time Complexity --> O(n)
- Insert: Space Complexity --> O(1)
    - at beginning: Time Complexity --> O(n)
    - at end: Time Complexity --> Dynamic --> O(1), Static --> O(n)
    - somewhere in between: Time Complexity --> O(n)
- Remove: Space Complexity --> O(1)
    - at beginning: Time Complexity --> O(n)
    - at end: Time Complexity --> O(1)
    - somewhere in between: Time Complexity --> O(n)

## Sorted Squared Array

- You are given an array of Integers in which each subsequent value is not less than the previous
  value.
- Write a function that takes this array as an input and returns a new array with the squares of
  each number sorted in ascending order.

## Monotonic Array

- An array is monotonic if it is either monotone increasing or monotone decreasing.
- An array is monotone increasing if all its elements from left to right are non-decreasing.
- An array is monotone decreasing if all its elements from left to right are non-increasing.
- Given an integer array return true if the given array is monotonic, or false otherwise. 

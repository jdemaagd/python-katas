# Searching

## Linear search algorithm

- Time Complexity -> O(n)
- Does not perform well when given list of data elements is large

## Jump search algorithm

- Divide sorted list of data into subsets of data elements called blocks
- Start comparing the search value with the last element of each block
    - if search value is less than last element of block, we compare it with next block
    - if search value is greater than last element of block, it means desired search value must be
      present in current block, apply linear search in this block and return index position
    - if search value is same as compared element of block, return index position of element and
      return candidate
- Generally, size of block is taken as sqrt of n , since it gives best performance for a given array
  of length n
- Time Complexity -> sqrt(n), where n size of block is sqrt(n)
- When given data elements are short and unsorted, better to use linear search algorithm

## Binary search algorithm

- List must be sorted
- Time Complexity -> O(log n)

## Interpolation search algorithm

- Works efficiently when there are uniformly distributed elements in the sorted list
- Compute starting search position depending on the item to be searched
- Steps
    - start searching for given search value from midpoint
    - if search value matches value stored at index of midpoint, return this index position
    - if search value does not match value stored at midpoint, divide list into two sub-lists, i.e.
      higher and lower sub-lists
    - if search value is greater than value of midpoint, search given search value in higher sublist
    - if search value is lower than value of midpoint, search given search value in lower sublist
    - repeat process until size of sub-lists is reduced to zero
- Average Time Complexity -> O(log(log(n))), where data set is sorted and uniformly distributed
- Worst Case Time Complexity -> O(n), where dataset is randomized
- Better than binary search and provides faster searching in most cases

## Exponential search algorithm

- Given sorted array of n data elements, first determine subrange in original list where desired
  search item may be present
- Next, use binary search algorithm to find out search value within subrange of data elements
  identified above
- Steps
    - check first element A[0] with search element
    - initialize index position i = 1
    - check two conditions
        - (1) end of array (i.e. 2^i < len(A))
            - check if we have searched complete list, and we stop if we have reached end of list
        - (2) not end of array (A[i] <= search_value)
            - stop searching when we reach an element whose value is greater than search value,
              because it means desired element will be present before this index position (since
              list is sorted)
    - if either of above two conditions is true, we move to next index position by incrementing `i`
      in powers of 2
    - stop when either of two conditions of above step is satisfied
    - apply binary search algorithm on range 2^i//2 to min (2^i, len(A))
- Time Complexity -> O(log base 2 i), where i is index where element to be searched is present

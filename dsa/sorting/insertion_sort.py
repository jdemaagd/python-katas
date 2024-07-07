"""
Insertion Sort (Stable)
Given an array of integers, write a function that will take this array as input and
return the sorted array using Insertion sort.
Divide array into 2 parts, sorted & non-sorted
Take elements from non-sorted part one-by-one and insert into sorted part

Stable Sorting Algorithm:
Initial relative ordering is maintained between duplicates
"""


# Time Complexity: O(n^2)
# Space Complexity: O(1)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


print(insertion_sort([1, 2, 8, 3, 7]))
print(insertion_sort([5, 4, 3, 2, 1]))

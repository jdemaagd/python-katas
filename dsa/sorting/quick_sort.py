"""
Quick Sort
Given an array of integers, write a function that will take this array as input and
return the sorted array using Quick sort.

Divide & Conquer Algorithm:
Select a pivot element from the array
All elements less than pivot are moved to left of pivot
All elements greater than pivot are moved to right of pivot
Use 2 pointers (`i' & `j`) at end and at next index past pivot
increment `i' until arr[i] > pivot
decrement `j' until arr[j] < pivot
swap arr[i] and arr[j]
repeat until i >= j
swap arr[i] and pivot
Recursively apply quick sort to left and right sub-array
"""


# Time Complexity: O(n log n), assumption that pivot is median
#     worst case, pivot is always smallest or largest element -> O(n^2)
# Space Complexity: O(log n), recursive call only on lower sized array
def quick_sort(array, start=0, end=None):
    if end is None:
        end = len(array) - 1

    while start < end:
        pivot_idx = partition(array, start, end)

        # Recursively call Quick Sort on lower sized subarray
        # Each recursion takes O(log(n)) in best case scenario and O(n) in worst case
        if pivot_idx - start < end - pivot_idx:
            quick_sort(array, start, pivot_idx - 1)
            start = pivot_idx + 1
        else:
            quick_sort(array, pivot_idx + 1, end)
            end = pivot_idx - 1

    return array


def swap(array, i, j):
    # This operation is O(1)
    array[i], array[j] = array[j], array[i]


def partition(array, start=0, end=None):
    if end is None:
        end = len(array) - 1

    # Finding middle takes O(1)
    middle = (start + end) // 2
    swap(array, start, middle)

    pivot = array[start]
    i = start + 1
    j = end

    while i <= j:
        # In worst case scenario, this can take O(n)
        while i <= j and array[i] <= pivot:
            i += 1
        while i <= j and array[j] > pivot:
            j -= 1
        if i < j:
            # This swap is O(1)
            swap(array, i, j)

    # This swap is O(1)
    swap(array, start, j)
    return j


print(quick_sort([1, 2, 8, 3, 7]))
print(quick_sort([6, 3, 1, 9, 5]))
print(quick_sort([14, 22, 12, 18, 19, 11, 8, 13, 9]))

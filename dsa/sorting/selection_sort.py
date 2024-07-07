"""
Selection Sort
Given an array of integers, write a function that will take this array as input and
return the sorted array using Selection sort.
In each pass, identify the smallest element and put it towards the front
"""


# Time Complexity: O(n^2)
# Space Complexity: O(1)
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # swap remaining smallest element with current element
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


print(selection_sort([1, 2, 8, 3, 7]))
print(selection_sort([5, 4, 3, 2, 1]))
print(selection_sort([5, 7, 1, 3, 2]))

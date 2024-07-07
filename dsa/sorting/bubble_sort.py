"""
Bubble Sort
Given an array of integers, write a function that will take this array as input and
return the sorted array using Bubble sort.
First pass: largest element bubbles up to the end of the array
Second pass: second-largest element bubbles up to the second last position
Continue this process until the array is sorted
"""


# Time Complexity: O(n^2)
# Space Complexity: O(1)
def bubble_sort_for(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


def bubble_sort_while(arr):
    is_sorted = False
    counter = 0

    while not is_sorted:
        is_sorted = True
        # using counter to track pass and decrement array length
        for i in range(len(arr) - 1 - counter):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = False
        counter += 1

    return arr


print(bubble_sort_for([1, 2, 8, 3, 7]))
print(bubble_sort_while([1, 2, 8, 3, 7]))

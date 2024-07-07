"""
Merge Sort (Stable)
Given an array of integers, write a function that will take this array as input and
return the sorted array using Merge sort.

Divide & Conquer Algorithm:
Divide: split array in half until size of array is 1
Conquer: merge sorted arrays

Stable Sorting Algorithm:
Initial relative ordering is maintained between duplicates
"""


# Time Complexity: O(n log n),
#     in each level visit n elements -> levels * n
#     num of levels -> 2^0 + 2^1 + 2^2 + ... + 2^k
#     n / 2^x, n / 2^x = 1, n = 2^x, x = log n
# Space Complexity: O(log n + n) -> O(n)
def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    left = nums[:mid]
    right = nums[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


# Time Complexity: O(n + m)
# Space Complexity: O(n + m)
def merge(left, right):     # sorted arrays
    result = []
    left_pointer = right_pointer = 0

    while left_pointer < len(left) and right_pointer < len(right):
        if left[left_pointer] < right[right_pointer]:
            result.append(left[left_pointer])
            left_pointer += 1
        else:
            result.append(right[right_pointer])
            right_pointer += 1

    result.extend(left[left_pointer:])
    result.extend(right[right_pointer:])

    return result


print(merge_sort([1, 2, 8, 3, 7]))

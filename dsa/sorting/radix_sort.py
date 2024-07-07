"""
Radix Sort
Given an array of non-negative integers, write a function that will take this array as input and
return the sorted array using Radix sort.
Sort based on units place, then tens place, then hundreds place, and so on.

Use counting sort (Stable)
Comparison based sorting algorithms -> O(n log n), best we can do w/o knowing anything about input
Numbers to sort lie between 0 and k (0 - 9), k is small
Count occurrence of each digit in input (frequency array) -> O(n)
Perform cumulative sum of frequency array -> O(k), where k is in range of digits (0 - 9)
Iterate given array in reverse, place elements in output array based on cumulative sum -> O(n)
Improved time complexity -> O(n + k) -> O(n)
Space complexity -> O(n + k) -> O(n)

Stable Sorting Algorithm:
Initial relative ordering is maintained between duplicates
"""


# Time Complexity: O(d * (n + k))
#     where d is number of digits in the largest number
# Space Complexity: O(n + k)
def radix_sort(array):
    # The space for array is O(n)
    if len(array) == 0:
        return 'empty array'

    greatest_number = max(array)
    number_of_digits = len(str(greatest_number))

    for i in range(number_of_digits):
        counting_sort(array, i)

    return array


def counting_sort(array, place):
    # The space for output and temp is O(n+k)
    output = [0] * len(array)
    temp = [0] * 10  # We're using base 10
    digit_place = 10 ** place

    for num in array:
        digit = (num // digit_place) % 10
        temp[digit] += 1

    for i in range(1, 10):
        temp[i] += temp[i - 1]

    for j in range(len(array) - 1, -1, -1):
        curr_digit = (array[j] // digit_place) % 10
        temp[curr_digit] -= 1
        insert_position = temp[curr_digit]
        output[insert_position] = array[j]

    array[:] = output[:]


print(radix_sort([7, 3, 2, 5, 1, 6]))
print(radix_sort([123, 78, 63, 19, 5]))
print(radix_sort([384, 73, 374, 183, 65, 247, 185]))

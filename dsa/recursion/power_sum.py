"""
Let's define a peculiar type of array in which each element is either an integer or another peculiar array.
Assume that a peculiar array is never empty.
Write a function that will take a peculiar array as its input and find the sum of its elements.
If an array is an element in the peculiar array you have to convert it to its equivalent value
so that you can sum it with the other elements.
Equivalent value of an array is the sum of its elements raised to the number which represents how far nested it is.
For e.g. [2, 3[4, 1, 2]] = 2 + 3 + (4 + 1 + 2) ^ 2
[1, 2, [7, [3, 4], 2]] = 1 + 2 + (7 + (3 + 4) ^ 3 + 2) ^ 2
"""


# Time complexity: O(n), where n is total elements in main and sub array
# Space complexity: O(d), where d is maximum depth of call stack
def power_sum(array, power=1):
    total = 0
    for i in array:
        if type(i) == list:     # element is an array
            total += power_sum(i, power + 1)
        else:
            total += i

    return total ** power


print(power_sum([2, 3, [4, 1, 2]]))         # 54
print(power_sum([1, 2, [7, [3, 4], 2]]))    # 123907
print(power_sum([1, 2, [3, 4], [[2]]]))     # 116

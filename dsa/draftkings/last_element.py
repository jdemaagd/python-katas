"""
Time Complexity: 𝑂(1),
  because accessing an element from a list by index (positive or negative) is a constant-time operation
Space Complexity: 𝑂(1),
  because no additional space is used beyond the input list
"""


def last_element(arr):
    return arr[-1]


# int_list = [0, 1, 2]
int_list = [0, 1, 2, 3, 4, 5, -7]
print(last_element(int_list))

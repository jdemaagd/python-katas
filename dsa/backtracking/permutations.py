"""
Given an array nums of distinct integers, return all the possible permutations.
You can return the answer in any order.
"""


# NOTE: n! -> distinct permutations
# Time complexity: O(n! * n)
# Space complexity: O(n) -> maximum depth of recursion
#   n! * n -> do not count space of answer we return
def permutation(nums):
    size = len(nums)
    res = []

    def helper(index):
        if index == size - 1:
            res.append(nums[:])
            return
        for j in range(index, size):                           # loop all possible choices
            nums[index], nums[j] = nums[j], nums[index]
            helper(index + 1)
            nums[index], nums[j] = nums[j], nums[index]         # backtracking step

    helper(0)
    return res


print(permutation([1, 2, 3]))
print(permutation([1, 2]))

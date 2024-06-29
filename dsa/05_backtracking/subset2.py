"""
Given an integer array nums that may contain duplicates, return all possible subsets (power set).
The solution set must not contain duplicate subsets.
Return the solution in any order.
"""


# Time complexity -> O(n * 2^n)
# Space complexity -> O(n) -> space on recursion stack
def subsets_with_duplicates(nums):
    res = []
    nums.sort()

    def subsets(index, curr):
        if index == len(nums):
            res.append(curr[:])
            return
        # include
        curr.append(nums[index])
        subsets(index + 1, curr)
        curr.pop()                      # backtracking step
        # exclude
        while index < len(nums) - 1 and nums[index] == nums[index + 1]:
            index += 1
        subsets(index + 1, curr)

    subsets(0, [])
    return res


print(subsets_with_duplicates([1, 2, 2]))
print(subsets_with_duplicates([1, 3, 3, 7]))

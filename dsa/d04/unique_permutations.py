"""
Given a collection of numbers, nums, that might contain duplicates, return all possible unique
  permutations in any order.
"""


# Time complexity: O(n! * n)
# Space complexity: O(n) -> maximum depth of recursion
def unique_permutations(nums):
    res = []

    def permutations(index):
        if index == len(nums) - 1:
            res.append(nums[:])
            return
        pairs = {}
        for j in range(index, len(nums)):
            if nums[j] not in pairs:
                pairs[nums[j]] = 1
                nums[index], nums[j] = nums[j], nums[index]
                permutations(index + 1)
                nums[index], nums[j] = nums[j], nums[index]     # backtracking step

    permutations(0)
    return res


print(unique_permutations([1, 1, 2]))

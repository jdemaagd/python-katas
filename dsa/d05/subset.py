"""
Given an integer array of unique elements, return all possible subsets (power set).
The solution set must not contain duplicate subsets.
Return the solution in any order.
"""


# Time complexity -> O(n * 2^n)
#   2^n subsets * for each subset calling function n times
# Space complexity: O(n) -> space on recursion stack
def power_set(nums):
    output = []

    def helper(nums1, i, subset):
        if i == len(nums1):
            output.append(subset.copy())
            return
        helper(nums1, i + 1, subset)        # exclude
        subset.append(nums1[i])             # include, this and next line
        helper(nums1, i + 1, subset)
        subset.pop()                        # backtracking step

    helper(nums, 0, [])
    return output


print(power_set([1, 2, 3]))
print(power_set([1, 8, 7]))

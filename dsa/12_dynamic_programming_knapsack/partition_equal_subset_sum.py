"""
Given an integer array `nums`, return `true` if you can partition the array into two subsets
such that the sum of the elements in both subsets is equal or `false` otherwise.
"""


def can_partition(nums):
    n = len(nums)
    sum_total = 0

    for num in nums:
        sum_total += num

    if sum_total % 2 != 0:
        return False

    target = sum_total // 2
    prev = [False] * (target + 1)
    curr = [False] * (target + 1)
    prev[0] = True
    curr[0] = True

    for i in range(1, n + 1):
        for j in range(1, target + 1):
            # pick
            if nums[i - 1] <= j:
                curr[j] = prev[j - nums[i - 1]]
            else:
                curr[j] = False
            curr[j] = curr[j] or prev[j]

        prev = curr[:]

    return curr[target]

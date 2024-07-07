"""
You are given an integer array `nums` and an integer `target`.
You want to build an `expression` out of nums by adding one of the symbols `+` and `-` before each
    integer in nums and then concatenate all the integers.
For example, if `nums = [2, 1]`, you can add a `+` before `2` and a `-` before `1` and concatenate
    them to build the expression `+2-1`.
Return the number of different `expressions` that you can build, which evaluates to `target`.
"""


def find_target_sum(nums, target):
    n = len(nums)
    summation = sum(nums)
    dp = [[None] * (2 * summation + 1) for _ in range(n)]

    def helper(index, sum_nums):
        if index < 0:
            if sum_nums == target:
                return 1
            else:
                return 0
        if dp[index][sum_nums + summation] is not None:
            return dp[index][sum_nums + summation]

        negative = helper(index - 1, sum_nums + -1 * nums[index])
        positive = helper(index - 1, sum_nums + nums[index])
        dp[index][sum_nums + summation] = negative + positive
        return dp[index][sum_nums + summation]

    return helper(n - 1, 0)


print(find_target_sum([1, 1, 1, 1, 1], 3))
print(find_target_sum([1], 1))
print(find_target_sum([1, 2, 3, 4, 5], 5))
print(find_target_sum([1, 2, 3, 4, 5], 10))


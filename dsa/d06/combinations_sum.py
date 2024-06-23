"""
Given an array of distinct integers candidates and a target integer target,
return a list of all unique combinations of candidates where the chosen numbers sum to target.
You may return the combinations in any order.
The same number may be chosen from candidates an unlimited number of times.
Two combinations are unique if the frequency of at least one of the chosen numbers is different.
"""


# Time complexity: O(n^(T/M + 1)),
#   where n is the number of candidates,
#   T is the target value,
#   and M is the minimal value among the candidates.
# Space complexity: O(T/M)
def combination_sum(candidates, target):
    res = []
    n = len(candidates)

    def helper(index, curr, curr_sum):
        if curr_sum > target:
            return
        if curr_sum == target:
            res.append(curr[:])
            return
        for j in range(index, n):
            curr.append(candidates[j])
            helper(j, curr, curr_sum + candidates[j])
            curr.pop()                                  # backtracking step

    helper(0, [], 0)
    return res


print(combination_sum([2, 3, 6, 7], 7))

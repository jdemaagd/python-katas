"""
Given a collection of candidate numbers (`candidates`) and a target number (`target`),
find all unique combinations in `candidates` where the candidate numbers sum to `target`.
Each number in `candidates` may only be used once in the combination.
Note: The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output:
    [
        [1,1,6],
        [1,2,5],
        [1,7],
        [2,6]
    ]

Example 2:
Input: candidates = [2,5,2,1,2], target = 5
Output:
    [
        [1,2,2],
        [5]
    ]

Constraints:
    1 <= candidates.length <= 100
    1 <= candidates[i] <= 50
    1 <= target <= 30

Combination Sum 1               vs      Combination Sum 2
distinct candidates                     candidates may have duplicates
use candidate multiple times            use candidate only once
"""


# Time Complexity -> O(n^2)
# Space Complexity -> O(n), max depth of recursion stack
def combination_sum2(candidates, target):
    res = []
    candidates.sort()
    n = len(candidates)

    def backtrack(index, curr_sum, curr):
        if curr_sum == target:
            res.append(curr[:])
            return
        if curr_sum > target:
            return              # prune this branch
        if index > n - 1:
            return              # array out of bounds

        my_hash = {}
        for j in range(index, n):
            if candidates[j] not in my_hash:
                my_hash[candidates[j]] = 1
                curr.append(candidates[j])
                backtrack(j + 1, curr_sum + candidates[j], curr)
                curr.pop()        # backtracking step

    backtrack(0, 0, [])

    return res


print(combination_sum2([10, 1, 2, 7, 6, 1, 5], 8))
print(combination_sum2([2, 5, 2, 1, 2], 5))
print(combination_sum2([2, 3, 4, 3, 5], 8))     # [[2, 3, 3], [3, 5]]

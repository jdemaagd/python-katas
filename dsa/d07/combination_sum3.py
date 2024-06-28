"""
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:
    Only numbers 1 through 9 are used.
    Each number is used at most once.
Return a list of all possible valid combinations.
The list must not contain the same combination twice, and the combinations may be returned in any order.

Example 1:
Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.

Example 2:
Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.

Example 3:
Input: k = 4, n = 1
Output: []
Explanation: There are no valid combinations.
Using 4 different numbers in the range [1,9],
  the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1,
  there are no valid combination.

Constraints:
    2 <= k <= 9
    1 <= n <= 60
"""


def combination_sum3(k, n):
    res = []

    def backtrack(number, curr, curr_sum):
        if curr_sum == n and len(curr) == k:
            res.append(curr[:])
            return
        if curr_sum > n or len(curr) == k:
            return
        for x in range(number, 10):
            curr.append(x)
            backtrack(x + 1, curr, curr_sum + x)
            curr.pop()

    backtrack(1, [], 0)

    return res


print(combination_sum3(3, 7))
print(combination_sum3(3, 9))
print(combination_sum3(4, 1))

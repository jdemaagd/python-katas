"""
You are provided with a set of N items, each with a specified weight and value.
Your objective is to pack these items into a backpack with a weight limit of W,
  maximizing the total value of items in the backpack.
Specifically, you have two arrays: val[0..N-1], representing the values of the items,
  and wt[0..N-1], indicating their weights.
Additionally, you have a weight limit W for the backpack.
The challenge is to determine the most valuable combination of items
  where the total weight does not exceed W.
Note that each item is unique and indivisible,
  meaning it must be either taken as a whole or left entirely.

Identify DP
choices: recursion (include/exclude)
optimal solution: maximize value that can be added to knapsack
"""


# Step 1: recursive solution
# Time Complexity: O(2^n), each item has 2 choices (include or exclude) n times
# Space Complexity: O(n), recursive call stack space
def knapsack_recursive(W, wt, val, n):
    def helper(index, rem_weight):
        # last valid input or first invalid input
        if index > n - 1 or rem_weight == 0:
            return 0

        exclude = helper(index + 1, rem_weight)
        include = 0
        if wt[index] <= rem_weight:
            include = val[index] + helper(index + 1, rem_weight - wt[index])

        return max(exclude, include)

    return helper(0, W)


# Step 2: memoization/top-down DP approach
# Time Complexity: O(n * W), n items and W weight, max upper bound
# Space Complexity: O(n * W), memoization table
def knapsack_memo(W, wt, val, n):
    mem2d = [[-1] * (W + 1) for _ in range(n)]

    def helper(index, rem_weight):
        if index > n - 1 or rem_weight == 0:
            return 0

        if mem2d[index][rem_weight] != -1:
            return mem2d[index][rem_weight]

        exclude = helper(index + 1, rem_weight)
        include = 0

        if wt[index] <= rem_weight:
            include = val[index] + helper(index + 1, rem_weight - wt[index])

        mem2d[index][rem_weight] = max(exclude, include)  # storing

        return mem2d[index][rem_weight]

    return helper(0, W)


# Step 3: tabulation/bottom-up DP approach
# Time Complexity: O(n * W), n items and W weight
# Space Complexity: O(n * W), tabulation table
def knapsack_tab(W, wt, val, n):
    tab2d = [[0] * (W + 1) for _ in range(n + 1)]

    # note: `i - 1` to consider 0-based indexing as dp table is 1-based
    for i in range(1, n + 1):
        for j in range(1, W + 1):
            exclude = tab2d[i - 1][j]
            include = 0
            if wt[i - 1] <= j:
                include = val[i - 1] + tab2d[i - 1][j - wt[i - 1]]
            tab2d[i][j] = max(exclude, include)

    return tab2d[n][W]


# Step 4: space-optimized tabulation
# Time Complexity: O(n * W), n items and W weight
# Space Complexity: O(W), tabulation table
def knapsack_space_optimized(W, wt, val, n):
    # 1D arrays to store rows
    prev = [0] * (W + 1)
    curr = [0] * (W + 1)

    for i in range(1, n + 1):
        for j in range(1, W + 1):
            exclude = prev[j]
            include = 0
            if wt[i - 1] <= j:
                include = val[i - 1] + prev[j - wt[i - 1]]
            curr[j] = max(exclude, include)
        prev = curr[:]

    return curr[W]


print(knapsack_recursive(50, [10, 20, 30], [60, 100, 120], 3))  # 220
print(knapsack_recursive(8, [8, 2, 5], [2, 3, 9], 3))  # 12
print()
print(knapsack_memo(50, [10, 20, 30], [60, 100, 120], 3))  # 220
print(knapsack_memo(8, [8, 2, 5], [2, 3, 9], 3))  # 12
print()
print(knapsack_tab(50, [10, 20, 30], [60, 100, 120], 3))  # 220
print(knapsack_tab(8, [8, 2, 5], [2, 3, 9], 3))  # 12
print()
print(knapsack_space_optimized(50, [10, 20, 30], [60, 100, 120], 3))  # 220
print(knapsack_space_optimized(8, [8, 2, 5], [2, 3, 9], 3))  # 12

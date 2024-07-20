"""
You are climbing a staircase
It takes n steps to reach the top
Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?

Identify DP problem:
Choice: at each step, we can take 1 or 2 steps
Notice overlapping subproblems
Application of Fibonacci

NOTE: Time/Space Complexity is same as Fibonacci Sequence
"""


# Step 1: start with recursive solution
def climb_stairs_recursive(n):
    if n < 3:
        return n

    return climb_stairs_recursive(n - 1) + climb_stairs_recursive(n - 2)


memo = {0: 0, 1: 1, 2: 2}


# Step 2: memoization/top-down DP approach
def climb_stairs_memo(n):
    if n in memo:
        return memo[n]
    else:
        memo[n] = climb_stairs_memo(n - 1) + climb_stairs_memo(n - 2)
        return memo[n]


# Step 3: tabulation/bottom-up DP approach
def climb_stairs_tab(n: int):
    if n == 0 or n == 1:
        return 1

    dp = [0] * (n + 1)

    # Base cases
    dp[0] = 1  # There's 1 way to stay at the ground (doing nothing)
    dp[1] = 1  # There's 1 way to reach the first step

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


# Step 4: space optimized tabulation
def climb_stairs_space_optimized(n: int):
    if n == 0 or n == 1:
        return 1

    curr, prev = 1, 1

    for _ in range(2, n + 1):
        nxt = curr + prev
        prev = curr
        curr = nxt

    return curr


# Alternative recursive solution
def climb_stairs(n):
    if n < 3:
        return n

    def helper(first, second, n2, curr):
        # subproblem
        # base condition
        nxt = first + second
        if curr == n2:
            return nxt

        return helper(second, nxt, n2, curr + 1)

    return helper(1, 2, n, 3)


print(climb_stairs_recursive(2))
print(climb_stairs_recursive(3))
print(climb_stairs_recursive(4))
print(climb_stairs_memo(5))
print(climb_stairs_memo(6))
print(climb_stairs_tab(7))
print(climb_stairs_tab(8))
print(climb_stairs_space_optimized(9))
print(climb_stairs_space_optimized(10))
print(climb_stairs(11))

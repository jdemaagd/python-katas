"""
The Tribonacci sequence Tn is defined as follows:
T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
Given n, return the value of Tn.
"""


# Step 1: recursive solution
# Time Complexity: O(3^n), each call potentially leads to 3 more calls
# Space Complexity: O(n), recursive call stack
def trib_recursive(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1

    return trib_recursive(n - 1) + trib_recursive(n - 2) + trib_recursive(n - 3)


# Step 2: memoization/top-down DP approach
# Time Complexity: O(n), compute once and store for each n (index)
# Space Complexity: O(n), max depth recursive call stack is n
def trib_memo(n):
    memo = [-1] * (n + 1)

    def helper(n2):
        if n2 == 0:
            return 0
        if n2 == 1 or n2 == 2:
            return 1

        if memo[n2] != -1:
            return memo[n2]

        memo[n2] = helper(n2 - 1) + helper(n2 - 2) + helper(n2 - 3)

        return memo[n2]

    return helper(n)


# Step 3: tabulation/bottom-up DP approach
# Time Complexity: O(n), compute once and store for each n (index)
# Space Complexity: O(n), store n + 1 elements in array
def trib_tab(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1

    dp = [0] * (n + 1)
    dp[0], dp[1], dp[2] = 0, 1, 1

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    return dp[n]


# Step 4: tabulation with space optimization
# Time Complexity: O(n), compute once and store for each n (index)
# Space Complexity: O(1), store only 3 elements
def tribonacci(n):
    zero = 0
    one = 1
    two = 1

    if n <= 1:
        return n
    if n == 2:
        return two

    for i in range(3, n + 1):
        nxt = zero + one + two
        zero = one
        one = two
        two = nxt

    return nxt


print(trib_recursive(4))  # 4
print(trib_recursive(25))  # 1389537
print()
print(trib_memo(4))  # 4
print(trib_memo(25))  # 1389537
print()
print(trib_tab(4))  # 4
print(trib_tab(25))  # 1389537
print()
print(tribonacci(4))  # 4
print(tribonacci(25))  # 1389537

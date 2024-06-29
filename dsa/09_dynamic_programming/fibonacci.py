"""
In Fibonacci sequence, each subsequent term is obtained by adding the preceding 2 terms
This is true for all the numbers except the first 2 numbers of the Fibonacci series
  as they do not have 2 preceding numbers
The first 2 terms in the Fibonacci series is `0` and `1` -> F(n) = F(n - 1) + F(n - 2) for n > 1
Write a function that finds `F(n)` given `n` where `n` is an integer greater than equal to 0
For the first term n = 0
"""


# Step 1: start with recursive solution
# Time Complexity: O(2^n)
#   each call branches into 2 calls almost n times
#   or looking each level -> 2^0 + 2^1 + 2^2 + ... + 2^(n - 1) = 2^n - 1
# Space Complexity: O(n)
#   recursive call stack will take order of n
#   max depth of the call stack is n
def fib_recursive(n):
    if n < 2:
        return n

    return fib_recursive(n - 1) + fib_recursive(n - 2)


memo = {0: 0, 1: 1}


# Step 2: memoization/top-down DP approach
# Time Complexity: O(n), n operations, retrieve every next value from hash/dict
# Space Complexity: O(n), hash table stores order of n, recursion call stack is order of n
def fib_memo(n):
    if n in memo:
        return memo[n]
    else:
        memo[n] = fib_memo(n - 1) + fib_memo(n - 2)
        return memo[n]


# Step 3: tabulation/bottom-up DP approach
# Time Complexity: O(n), n operations
# Space Complexity: O(n), 1d table array of size n
def fib_tab(n):
    tab1d = [0] * (n + 1)

    if n > 0:
        tab1d[1] = 1

    count = 1
    while count < n:
        count += 1
        tab1d[count] = tab1d[count - 1] + tab1d[count - 2]

    return tab1d[n]


# Step 4: space optimized tabulation
# Time Complexity: O(n), n operations
# Space Complexity: O(1), only 2 variables
def fib_space_optimized(n):
    if n < 2:
        return n

    prev = 0
    curr = 1

    counter = 1
    while counter < n:
        nxt = prev + curr
        counter += 1
        prev = curr
        curr = nxt

    return curr


print(fib_recursive(7))  # 0, 1, 1, 2, 3, 5, 8, 13
print(fib_memo(9))  # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
print(fib_tab(11))  # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
print(fib_space_optimized(13))  # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233

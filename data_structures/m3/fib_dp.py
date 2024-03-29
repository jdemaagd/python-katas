def fib_dp(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if lookup[n] is not None:
        return lookup[n]

    lookup[n] = fib_dp(n - 1) + fib_dp(n - 2)
    return lookup[n]


lookup = [None] * 1000

for i in range(6):
    print(fib_dp(i))

# Time complexity: O(n)

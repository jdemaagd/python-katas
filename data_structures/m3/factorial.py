def factorial(n):
    # test for a base case
    if n == 0:
        return 1
    else:
        # make a calculation and a recursive call
        return n * factorial(n - 1)


print(factorial(4))

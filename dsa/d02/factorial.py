def seq(n):
    if n == 0:
        return

    print(n)
    seq(n - 1)
    print(n)


# NOTE: 0 to n recursive approach
def sum_inc(start, end):
    if start == end:
        return end

    return start + sum_inc(start + 1, end)


# NOTE: n to 0 recursive approach
def sum_dec(end):
    if end == 0:
        return 0

    return end + sum_dec(end - 1)


def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n - 1)


def fibonacci(n):
    if n < 2:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


seq(4)
print()
print(sum_inc(0, 5))
print()
print(sum_dec(5))
print()

print(factorial(7))
print(fibonacci(12))

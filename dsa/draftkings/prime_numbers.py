def prime_numbers(n):
    primes = []
    sieve = [True] * (n + 1)
    sieve[0], sieve[1] = False, False

    for num in range(2, int(n ** 0.5) + 1):
        if sieve[num]:
            primes.append(num)
            for multiple in range(num * num, n + 1, num):
                sieve[multiple] = False

    for num in range(int(n ** 0.5) + 1, n + 1):
        if sieve[num]:
            primes.append(num)

    return primes


# Test the function
N = 20
print(prime_numbers(N))

"""
Time Complexity
1. Initialization -> initializes a list of True values with a length of 𝑛 + 1 -> O(𝑛)
2. Marking Non-Primes
   Outer Loop -> runs from 2 to √𝑛 -> O(√𝑛)
   Inner Loop -> marks multiples of num as False
     for each prime num, it marks approximately 𝑛 − 𝑛𝑢𝑚^2 / 𝑛𝑢𝑚 numbers as `False`
     summing over all primes, this operation will roughly run in 𝑂(𝑛 log log 𝑛) time
       due to the harmonic series nature of the marking process
3. Collecting Remaining Primes
   Loop: runs from √𝑛 to 𝑛 -> O(𝑛), but most values are checked quickly if they are still `True`
Combining these steps, total time complexity is dominated by marking process in Sieve of Eratosthenes -> O(𝑛 log log 𝑛)

Space Complexity
1. Sieve List -> 𝑂(𝑛)
2. Primes List -> in the worst case, `𝑛`
   approximation: number of primes up to `n` is 𝑂(𝑛 / log 𝑛)
"""


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

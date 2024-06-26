"""
calculates the sample variance of a list of numbers

Time Complexity -> 𝑂(𝑛)
1. Compute Length -> `len` function runs in 𝑂(1) time as it simply returns stored length of list
2. Compute Mean -> `sum` function iterates through list to sum all elements, which takes 𝑂(𝑛) time
   division by 𝑛 is 𝑂(1) time
   overall, computing the mean takes 𝑂(𝑛) time
3. Compute Variance -> `sum` function then sums these 𝑛 values, taking 𝑂(𝑛) time
   generator expression `(x - mean) ** 2 for x in arr` iterates through list,
     calculating squared difference for each element -> 𝑂(𝑛) time
   division by 𝑛 − 1 is 𝑂(1) time
   overall, computing the variance takes 𝑂(𝑛) time
Combining these steps, total time complexity of `get_variance` function -> 𝑂(1) + 𝑂(𝑛) + 𝑂(𝑛) = 𝑂(𝑛)

Space Complexity -> 𝑂(1)
1. Storage for Variables: `n` and `mean` are scalars and take 𝑂(1) space each
2. Storage for Intermediate Results: `sum` function accumulates the result using constant space
   generator expression `(x - mean) ** 2 for x in arr` does not create a new list but generates
     each squared difference on the fly, using 𝑂(1) additional space
3. Return Value: value variance is a scalar and takes 𝑂(1) space
"""


def get_variance(arr):
    n = len(arr)
    mean = sum(arr) / n
    variance = sum((x - mean) ** 2 for x in arr) / (n - 1)
    return variance


test_list = [6, 7, 3, 9, 10, 15]
print(get_variance(test_list))

# Output: 13.89

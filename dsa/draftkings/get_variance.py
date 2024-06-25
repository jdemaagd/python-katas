def get_variance(arr):
    n = len(arr)
    mean = sum(arr) / n
    variance = sum((x - mean) ** 2 for x in arr) / (n - 1)
    return variance


test_list = [6, 7, 3, 9, 10, 15]
print(get_variance(test_list))

# Output: 13.89

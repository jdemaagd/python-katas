# Time complexity: sort + linear --> O(n) + O(n log n) --> O(n log n)
# Space complexity: O(n)
def brute_squared(arr):
    n = len(arr)
    res = [0] * n
    for i in range(n):
        res[i] = arr[i] ** 2
    res.sort()
    return res
    # return [i**2 for i in arr]


# Time complexity: O(n)
# Space complexity: O(n)
def two_pointer_squared(array):
    size = len(array)
    start, end = 0, size - 1
    result = [0] * size

    for k in reversed(range(size)):
        i_squared = array[start] ** 2
        j_squared = array[end] ** 2
        if i_squared > j_squared:
            result[k] = i_squared
            start += 1  # move starting pointer towards the end of array
        else:
            result[k] = j_squared
            end -= 1    # move ending pointer towards the start of array

    return result


squares = brute_squared([1, 2, 3, 4, 5])
print(squares)  # [1, 4, 9, 16, 25]

print(two_pointer_squared([-5, -4, -2, 1, 9, 12]))

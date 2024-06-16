def brute_monotonic(arr):
    if not arr:
        return True

    increasing = decreasing = True
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            increasing = False
        if arr[i] > arr[i - 1]:
            decreasing = False

    return increasing or decreasing


# Time complexity: O(n)
# Space complexity: O(1)
def monotonic_array(arr):
    n = len(arr)
    if (n == 0) or (n == 1):
        return True

    first = arr[0]
    last = arr[n - 1]

    if first > last:    # monotonic decreasing or not monotonic
        for k in range(n - 1):
            if arr[k] < arr[k + 1]:
                return False
    elif first < last:  # monotonic increasing or not monotonic
        for k in range(n - 1):
            if arr[k] > arr[k + 1]:
                return False
    else:               # monotonic, all values are equal
        for k in range(n - 1):
            if arr[k] != arr[k + 1]:
                return False

    return True


print(monotonic_array([1, 2, 2, 3]))  # True
print(monotonic_array([3, 3, 3]))  # True
print(monotonic_array([7]))  # True
print(monotonic_array([]))  # True
print(monotonic_array([2, 2, 3, 1]))  # False

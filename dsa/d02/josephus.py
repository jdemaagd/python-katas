# Time Complexity: O(n^2)
# Space complexity: O(n)
def approach1(n, k):
    arr = [i + 1 for i in range(n)]

    def helper(arr1, start_index):
        if len(arr1) == 1:
            return arr1[0]
        index_to_remove = (start_index + k - 1) % len(arr1)
        del arr1[index_to_remove]
        return helper(arr1, index_to_remove)

    return helper(arr, 0)


# Time Complexity: O(n)
# Space complexity: O(n)
def approach2(n, k):    # using solution to sub-problem to solve original problem
    def josephus(n1):
        if n1 == 1:
            return 0
        return (josephus(n1 - 1) + k) % n1

    return josephus(n) + 1


# Time Complexity: O(n)
# Space complexity: O(1)
def approach3(n, k):    # improve space complexity of recursive call stack
    survivor = 0
    for i in range(2, n + 1):
        survivor = (survivor + k) % i

    return survivor + 1


print(approach3(5, 2))  # 3
print(approach3(6, 5))  # 1

"""
You are given an integer array cost where `cost[i]` is the cost of `ith` step on a staircase.
Once you pay the cost, you can either climb one or two steps.
You can either start from the step with index 0, or the step with index 1.
Return the minimum cost to reach the top of the floor.
"""


# Step 1: recursive solution
# Time Complexity: O(2^n), each call potentially leads to 2 more calls
# Space Complexity: O(n), recursive call stack
def cost_from_recursive(cost):
    n = len(cost)

    def helper(index):
        if index >= n:
            return 0

        one = cost[index] + helper(index + 1)
        two = cost[index] + helper(index + 2)

        return min(one, two)

    return min(helper(0), helper(1))


# Step 2: memoization/top-down DP approach
# Time Complexity: O(n), compute once and store for each n (index)
# Space Complexity: O(n), max depth recursive call stack is n
def cost_from_memo(cost):
    n = len(cost)
    array = [-1] * n  # memo store

    def helper(index):
        if index >= n:
            return 0

        if array[index] != -1:
            return array[index]

        one = cost[index] + helper(index + 1)
        two = cost[index] + helper(index + 2)
        array[index] = min(one, two)

        return array[index]

    return min(helper(0), helper(1))


# Step 3: tabulation/bottom-up DP approach
# Time Complexity: O(n), compute once and store for each n (index)
# Space Complexity: O(n), store n + 1 elements in array
def min_cost_tab(cost):
    n = len(cost)

    min_cost = [-1] * (n + 1)

    min_cost[0] = 0
    min_cost[1] = 0

    for i in range(2, n + 1):
        prevOne = cost[i - 1] + min_cost[i - 1]
        prevTwo = cost[i - 2] + min_cost[i - 2]
        min_cost[i] = min(prevOne, prevTwo)

    return min_cost[n]


# Step 4: tabulation with space optimization
# Time Complexity: O(n), compute once and store for each n (index)
# Space Complexity: O(1), store only 3 elements
def min_cost_space_optimized(cost):
    n = len(cost)

    curr = 0
    prev = 0

    for i in range(2, n + 1):
        nxt = min(cost[i - 1] + curr, cost[i - 2] + prev)
        prev = curr
        curr = nxt

    return curr


print(cost_from_recursive([10, 15, 20]))  # 15
print(cost_from_recursive([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))  # 6
print()
print(cost_from_memo([10, 15, 20]))  # 15
print(cost_from_memo([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))  # 6
print()
print(min_cost_tab([10, 15, 20]))  # 15
print(min_cost_tab([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))  # 6
print()
print(min_cost_space_optimized([10, 15, 20]))  # 15
print(min_cost_space_optimized([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))  # 6

"""
Given a set of N items, each with a weight and a value, represented by the array wt and val
respectively.
Also, a knapsack with weight limit W. The task is to fill the knapsack in such a way that we can get
the maximum profit.
Return the maximum profit.
Note: Each item can be taken `any number of times`.
"""


def unbounded_knapsack_tab(N, wt, val, W):
    tab2d = [[0] * (W + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, W + 1):
            exclude = tab2d[i - 1][j]
            include = 0
            if wt[i - 1] <= j:
                include = val[i - 1] + tab2d[i][j - wt[i - 1]]
            tab2d[i][j] = max(exclude, include)

    return tab2d[N][W]


# Time Complexity: O(n * W), n * W cells in tabulation
# Space Complexity: O(W)
def unbounded_knapsack_tab2(N, wt, val, W):
    tab2d = [[-1] * (W + 1) for _ in range(N + 1)]

    for j in range(W + 1):
        tab2d[0][j] = 0

    for i in range(N + 1):
        tab2d[i][0] = 0

    for i in range(1, N + 1):
        for j in range(1, W + 1):
            exclude = tab2d[i - 1][j]
            include = 0
            if wt[i - 1] <= j:
                include = val[i - 1] + tab2d[i][j - wt[i - 1]]
            tab2d[i][j] = max(exclude, include)

    return tab2d[N][W]


print(unbounded_knapsack_tab(3, [8, 2, 5], [2, 4, 9], 8))       # 16

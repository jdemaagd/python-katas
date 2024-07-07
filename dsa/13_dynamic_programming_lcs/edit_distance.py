"""
Given two strings word1 and word2,
return the minimum number of operations required to convert word1 to word2.
You have the following three operations permitted on a word:
    - Insert a character
    - Delete a character
    - Replace a character
"""


# Step 1: recursive solution
# Time Complexity: O(3^(m + n)), where m and n are the lengths of the two strings
# Space Complexity: O(m + n)
def min_distance_recursive(word1, word2):
    n = len(word1)
    m = len(word2)

    def number_of_operations(n_index, m_index):
        if n_index > n - 1 and m_index > m - 1:
            return 0
        if n_index > n - 1:
            return m - m_index
        if m_index > m - 1:
            return n - n_index

        if word1[n_index] == word2[m_index]:
            return number_of_operations(n_index + 1, m_index + 1)

        insert = 1 + number_of_operations(n_index, m_index + 1)
        delete = 1 + number_of_operations(n_index + 1, m_index)
        replace = 1 + number_of_operations(n_index + 1, m_index + 1)

        return min(insert, delete, replace)

    return number_of_operations(0, 0)


# Step 2: memoization/top-down approach
# Time Complexity: O(m * n), where m and n are the lengths of the two strings
# Space Complexity: O(m * n)
def min_distance_memo(word1, word2):
    n = len(word1)
    m = len(word2)
    memo = [[-1] * m for _ in range(n)]

    def helper(n_index, m_index):
        if n_index < 0:
            return m_index + 1
        if m_index < 0:
            return n_index + 1

        if memo[n_index][m_index] != -1:
            return memo[n_index][m_index]

        if word1[n_index] == word2[m_index]:
            memo[n_index][m_index] = helper(n_index - 1, m_index - 1)
            return memo[n_index][m_index]

        replace = 1 + helper(n_index - 1, m_index - 1)
        delete = 1 + helper(n_index - 1, m_index)
        insert = 1 + helper(n_index, m_index - 1)
        memo[n_index][m_index] = min(replace, delete, insert)

        return memo[n_index][m_index]

    return helper(n - 1, m - 1)


# Step 3: tabulation/bottom-up approach
# Time Complexity: O(m * n), where m and n are the lengths of the two strings
# Space Complexity: O(m * n)
def min_distance_tab(word1, word2):
    n = len(word1)
    m = len(word2)

    tab2d = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        tab2d[i][0] = i

    for j in range(m + 1):
        tab2d[0][j] = j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if word1[i - 1] == word2[j - 1]:
                tab2d[i][j] = tab2d[i - 1][j - 1]               # characters are equal (diagonal)
            else:
                replace = 1 + tab2d[i - 1][j - 1]               # replace (diagonal)
                delete = 1 + tab2d[i - 1][j]                    # delete (top)
                insert = 1 + tab2d[i][j - 1]                    # insert (left)
                tab2d[i][j] = min(delete, replace, insert)

    return tab2d[n][m]


# Step 4: space optimized tabulation
# Time Complexity: O(m * n), where m and n are the lengths of the two strings
# Space Complexity: O(m)
def min_distance_space_optimized(word1, word2):
    n = len(word1)
    m = len(word2)

    prev = [0] * (m + 1)
    curr = [0] * (m + 1)

    for j in range(m + 1):
        prev[j] = j

    for i in range(1, n + 1):
        curr[0] = i
        for j in range(1, m + 1):
            if word1[i - 1] == word2[j - 1]:
                curr[j] = prev[j - 1]
            else:
                replace = 1 + prev[j - 1]
                delete = 1 + prev[j]
                insert = 1 + curr[j - 1]
                curr[j] = min(delete, replace, insert)
        prev = curr[:]

    return prev[m]


print(min_distance_recursive("horse", "ros"))  # 3
print(min_distance_recursive("intention", "execution"))  # 5
print(min_distance_recursive("table", "bel"))  # 3
print()
print(min_distance_memo("horse", "ros"))  # 3
print(min_distance_memo("intention", "execution"))  # 5
print(min_distance_memo("table", "bel"))  # 3
print()
print(min_distance_tab("horse", "ros"))  # 3
print(min_distance_tab("intention", "execution"))  # 5
print(min_distance_tab("table", "bel"))  # 3
print()
print(min_distance_space_optimized("horse", "ros"))  # 3
print(min_distance_space_optimized("intention", "execution"))  # 5
print(min_distance_space_optimized("table", "bel"))  # 3

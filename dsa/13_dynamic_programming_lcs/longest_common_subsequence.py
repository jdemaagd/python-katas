"""
Given two strings text1 and text2, return the length of their longest common subsequence.
If there is no common subsequence, return 0.
A subsequence of a string is a new string generated from the original string with some characters
    (can be none) deleted without changing the relative order of the remaining characters.
For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

Identify as a Dynamic Programming problem:
    - involves choices -> include/exclude
    - and asked to find an optimal solution -> the longest common subsequence
"""


# Step 1: Recursion
# Time Complexity: O(2^(n + m)) -> 2 * 2 * 2 * ... (n + m) times
# Space Complexity: O(n + m)
def longest_common_subsequence_recursive(text1, text2):
    n = len(text1)
    m = len(text2)

    def helper(n_index, m_index):
        if n_index > n - 1 or m_index > m - 1:
            return 0

        if text1[n_index] == text2[m_index]:
            return 1 + helper(n_index + 1, m_index + 1)

        return max(helper(n_index + 1, m_index), helper(n_index, m_index + 1))

    return helper(0, 0)


# Step 2: memoization/top-down approach
# Time Complexity: O(n * m) -> n * m subproblems
# Space Complexity: O(n * m) + O(n + m), memo table + recursion stack, -> O(n * m)
def longest_common_subsequence_memo(text1, text2):
    n = len(text1)
    m = len(text2)
    memo = [[-1] * m for _ in range(n)]

    def helper(n_index, m_index):
        # base case
        if n_index > n - 1 or m_index > m - 1:
            return 0

        if memo[n_index][m_index] != -1:
            return memo[n_index][m_index]

        # recursive case
        if text1[n_index] == text2[m_index]:
            memo[n_index][m_index] = 1 + helper(n_index + 1, m_index + 1)
            return memo[n_index][m_index]

        memo[n_index][m_index] = max(helper(n_index + 1, m_index), helper(n_index, m_index + 1))

        return memo[n_index][m_index]

    return helper(0, 0)


# Step 3: tabulation/bottom-up approach
# Time Complexity: O(n * m) -> n * m subproblems
# Space Complexity: O(n * m) -> memo table
def longest_common_subsequence_tab(text1, text2):
    n = len(text1)
    m = len(text2)
    tab2d = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if text1[i - 1] == text2[j - 1]:
                tab2d[i][j] = 1 + tab2d[i - 1][j - 1]
            else:
                tab2d[i][j] = max(tab2d[i - 1][j], tab2d[i][j - 1])

    return tab2d[n][m]


# Step 4: space optimized tabulation
# Time Complexity: O(n * m) -> n * m subproblems
# Space Complexity: O(m) -> memo table
def longest_common_subsequence_space_optimized(text1, text2):
    n = len(text1)
    m = len(text2)

    prev = [0] * (m + 1)
    curr = [0] * (m + 1)

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if text1[i - 1] == text2[j - 1]:
                curr[j] = 1 + prev[j - 1]
            else:
                curr[j] = max(prev[j], curr[j - 1])
        prev = curr[:]

    return curr[m]


print(longest_common_subsequence_recursive("abcdef", "acef"))  # 4
print(longest_common_subsequence_recursive("abcdef", "rabc"))  # 3
print(longest_common_subsequence_recursive("abc", "abc"))  # 3
print()
print(longest_common_subsequence_memo("abcdef", "acef"))  # 4
print(longest_common_subsequence_memo("abcdef", "rabc"))  # 3
print(longest_common_subsequence_memo("abc", "abc"))  # 3
print()
print(longest_common_subsequence_tab("pqrst", "prt"))  # 3
print(longest_common_subsequence_tab("abcdef", "acef"))  # 4
print(longest_common_subsequence_tab("abcdef", "rabc"))  # 3
print()
print(longest_common_subsequence_space_optimized("abcdef", "acef"))  # 4
print(longest_common_subsequence_space_optimized("abcdef", "rabc"))  # 3
print(longest_common_subsequence_space_optimized("abc", "abc"))  # 3

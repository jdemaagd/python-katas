"""
Time Complexity
1. Outer Loop (over `str1`) -> iterates `i` over all indices of `str1` -> O(n)
2. Inner Loop (over `str2`) -> iterates `j` over all indices of `str2` -> O(m)
3. While Loop (matching substrings) -> iterates `k`
   as long as characters in `str1` and `str2` match starting from `i` and `j`
   worst-Case Time Complexity: 𝑂(min(𝑛 − 𝑖, 𝑚 − 𝑗))
   this loop could run for the length of the shorter suffix of `str1` or `str2` starting from indices `i` and `j`
Combined -> 𝑂(𝑛 * 𝑚 * min(𝑛, 𝑚)) -> since min(𝑛, 𝑚) <= min(𝑛, 𝑚)
   let n = min(𝑛, 𝑚)
   let m = max(𝑛, 𝑚)
   in worst case -> 𝑂(n^3)

Space Complexity -> 𝑂(n) in worst case
1. Space for `max_substring`
   variable: stores the longest common substring found so far
   O(n) in the worst case, where 𝑛 is the length of the longest common substring
2. No Additional Data Structures -> 𝑂(1)
"""


def maximal_substring(str1, str2):
    max_substring = ''
    for i in range(len(str1)):
        for j in range(len(str2)):
            k = 0
            while i + k < len(str1) and j + k < len(str2) and str1[i + k] == str2[j + k]:
                k += 1
            if k > len(max_substring):
                max_substring = str1[i:i + k]
    return max_substring


# Test the function
string1 = 'mississippi'
string2 = 'mossyistheapple'
print(maximal_substring(string1, string2))
# Output: 'ssis'

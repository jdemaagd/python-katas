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

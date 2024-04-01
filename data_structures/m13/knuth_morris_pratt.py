# NOTE: generate prefix function for given pattern
def prefix_function(pattern):
    n = len(pattern)
    prefix_fun = [0] * n
    k = 0

    for q in range(2, n):
        while k > 0 and pattern[k + 1] != pattern[q]:
            k = prefix_fun[k]
        if pattern[k + 1] == pattern[q]:
            k += 1
        prefix_fun[q] = k

    return prefix_fun


def kmp_matcher(text, pattern):
    m = len(text)
    n = len(pattern)
    flag = False
    text = '-' + text  # append dummy character to make it 1-based indexing
    pattern = '-' + pattern  # append dummy character to the pattern also
    prefix_fun = prefix_function(pattern)
    q = 0
    for i in range(1, m + 1):
        # while pattern and text are not equal, decrement value of q if it is > 0
        while q > 0 and pattern[q + 1] != text[i]:
            q = prefix_fun[q]
        if pattern[q + 1] == text[i]:
            q += 1
        if q == n:
            print("Pattern occurs with shift", i - n)
            flag = True
            q = prefix_fun[q]
    if not flag:
        print('\nNo match found')


kmp_matcher('aabaacaadaabaaba', 'aabaa')

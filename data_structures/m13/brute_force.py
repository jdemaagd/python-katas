def brute_force(text, pattern):
    l1 = len(text)
    l2 = len(pattern)
    i = 0
    j = 0
    flag = False  # if pattern does not appear at all, then set this to false and execute last if statement

    while i < l1:
        j = 0
        count = 0
        while j < l2:
            if i + j < l1 and text[i + j] == pattern[j]:
                count += 1
            j += 1
        if count == l2:  # it shows a matching of pattern in text
            print("\nPattern occurs at index", i)
            flag = True
            # flag is True as we wish to continue looking for more matching of pattern in text
        i += 1
    if not flag:
        # if pattern does not occur at all, means no match of pattern in text string
        print('\nPattern is not at all present in the array')


brute_force('acbcabccababcaacbcac', 'acbcac')

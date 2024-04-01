text = "acbaacacababacacac"
pattern = "acacac"

matched_indexes = []

i = 0
flag = True
while i <= len(text) - len(pattern):
    for j in range(len(pattern) - 1, -1, -1):
        if pattern[j] != text[i + j]:
            flag = False
            if j == len(pattern) - 1:  # if good-suffix is not present, test bad character
                if text[i + j] in pattern[0:j]:
                    # NOTE: i+j is index of bad character,
                    # jumping pattern to match bad character of text with same character in pattern
                    i = i + j - pattern[0:j].rfind(text[i + j])
                else:
                    # NOTE: if bad character is not present, jump pattern next to it
                    i = i + j + 1
            else:
                k = 1
                while text[i + j + k:i + len(pattern)] not in pattern[0:len(pattern) - 1]:
                    # used for finding sub part of a good-suffix
                    k = k + 1
                if len(text[i + j + k:i + len(pattern)]) != 1:  # good-suffix should not be of one character
                    gs_shift = i + j + k - pattern[0:len(pattern) - 1].rfind(text[i + j + k:i + len(pattern)])
                    # jumps pattern to position where good-suffix of pattern matches with good-suffix of text
                else:
                    # NOTE: when good-suffix heuristic is not applicable,
                    #       prefer bad character heuristic
                    gs_shift = 0  #

                if text[i + j] in pattern[0:j]:
                    # NOTE: i+j is index of bad character,
                    # jumping pattern to match bad character of text with same character in pattern
                    bc_shift = i + j - pattern[0:j].rfind(text[i + j])
                else:
                    bc_shift = i + j + 1
                i = max((bc_shift, gs_shift))
            break
    if flag:
        matched_indexes.append(i)
        i = i + 1
    else:
        flag = True

print("Pattern found at", matched_indexes)

def generate_hash(text, pattern):
    ord_text = [ord(i) for i in text]  # stores unicode value of each character in text
    ord_pattern = [ord(j) for j in pattern]  # stores unicode value of each character in pattern
    len_text = len(text)
    len_pattern = len(pattern)
    len_hash_array = len_text - len_pattern + 1  # stores length of new array that will contain hash values of text
    hash_text = [0] * len_hash_array
    hash_pattern = sum(ord_pattern)
    for i in range(0, len_hash_array):  # step size of loop will be size of pattern
        if i == 0:
            hash_text[i] = sum(ord_text[:len_pattern])  # initial value of hash function
        else:
            hash_text[i] = ((hash_text[i - 1] - ord_text[i - 1]) + ord_text[
                i + len_pattern - 1])  # calculating next hash value using previous value
    return [hash_text, hash_pattern]  # return hash values


def rabin_karp_matcher(text, pattern):
    text = str(text)
    pattern = str(pattern)
    hash_text, hash_pattern = generate_hash(text, pattern)
    len_text = len(text)
    len_pattern = len(pattern)
    flag = False  # checks if pattern is present at least once or not at all
    for i in range(len(hash_text)):
        if hash_text[i] == hash_pattern:  # if the hash value matches
            count = 0
            for j in range(len_pattern):
                if pattern[j] == text[i + j]:
                    count += 1
                else:
                    break
            if count == len_pattern:
                flag = True
                print('Pattern occurs at index', i)
    if not flag:
        print('Pattern is not at all present in the text')


rabin_karp_matcher("101110000011010010101101", "10112")

# Works for numeric
rabin_karp_matcher("101110000011010010101101", "1011")

# Works for alphabets
rabin_karp_matcher("ABBACCADABBACCEDF", "ACCE")

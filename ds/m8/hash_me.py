my_dict = {"Basant": "9829012345", "Ram": "9829012346", "Shyam": "9829012347", "Sita": "9829012348"}

print("All keys and values")
for x, y in my_dict.items():
    print(x, ":", y)  # prints keys and values
my_dict["Ram"]

print()
hash1 = sum(map(ord, 'hello world'))
print(hash1)

# h   e   l   l   o          w   o   r   l   d
# 104 101 108 108 111   32   119 111 114 108 100 = 1116

# NOTE: collision
hash2 = sum(map(ord, 'gello xorld'))
print(hash2)


# h   e   l   l   o          w   o   r    l    d
# 104 101 108 108 111   32   119 111 114  108  100  -> 1116
# 1   2   3   4   5     6    7   8   9    10   11   -> multiplier
# 104 202 324 432 555   192  833 888 1026 1080 1100 -> 6736

def my_hash(s):
    mult = 1
    hv = 0
    for ch in s:
        hv += mult * ord(ch)
        mult += 1
    return hv


print()
for item in ('hello world', 'world hello', 'gello xorld'):
    print("{}: {}".format(item, my_hash(item)))

print("\nImperfect Hash...")
for item in ('ad', 'ga'):
    print("{}: {}".format(item, my_hash(item)))

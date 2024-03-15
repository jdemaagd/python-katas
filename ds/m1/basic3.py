###### Ordered List ######
[10, 12, 31, 14] == [14, 10, 31, 12]
print([10, 12, 31, 14] == [14, 10, 31, 12])
# False

###### Dynamic List ######
b = ['data', 'and', 'book', 'structure', 'hello', 'st']

b += [32]
print(b)
# ['data', 'and', 'book', 'structure', 'hello', 'st', 32]


b[2:3] = []
print(b)
# ['data', 'and', 'structure', 'hello', 'st', 32]

del b[0]
print(b)
# ['and', 'structure', 'hello', 'st', 32]

a = [2.2, 'python', 31, 14, 'data', False, 33.59]
print(a)
# [2.2, 'python', 31, 14, 'data', False, 33.59]

a = ['data', 'structures', 'using', 'python', 'happy', 'learning']
print(a[0])
'data'
print(a[2])
'using'
print(a[-1])
'learning'
print(a[-5])
'structures'

print(a[1:5])
['structures', 'using']

print(a[-3:-1])
['python', 'happy']

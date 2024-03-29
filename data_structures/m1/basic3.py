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

a = ['data', 'and', 'book', 'structure', 'hello', 'st']
print(a)
['data', 'and', 'book', 'structure', 'hello', 'st']
a[1] = 1
a[-1] = 120
print(a)
['data', 1, 'book', 'structure', 'hello', 120]

a = ['data', 'and', 'book', 'structure', 'hello', 'st']

print(a[2:5])
['book', 'structure', 'hello']
a[2:5] = [1, 2, 3, 4, 5]
print(a)
['data', 'and', 1, 2, 3, 4, 5, 'st']

a = ['data', 'structures', 'using', 'python', 'happy', 'learning']
print('data' in a)
# True

print(a)
# ['data', 'structures', 'using', 'python', 'happy', 'learning']

a + ['New', 'elements']
print(a)
# ['data', 'structures', 'using', 'python', 'happy', 'learning', 'New', 'elements']

print(a * 2)
# ['data', 'structures', 'using', 'python', 'happy', 'learning', 'New', 'elements', 'data', 'structures', 'using',
# 'python', 'happy', 'learning', 'New', 'elements']

print(len(a))
# 6
print(min(a))

str1 = 'Hello how are you'
str2 = "Hello how are you"
str3 = 'multiline' + 'string';
print(str1)
print(str2)
print(str3)

f = 'data'
s = 'structure'
print(f + s)
# 'datastructure'
print('Data ' + 'structure')
# Data structure

st = 'data.'
print(st * 3)
# 'data.data.data.'
print(3 * st)
# 'data.data.data.'

###### Range ######

print(list(range(10)))
print(range(10))
print(list(range(10)))
print(range(1, 10, 2))
print(list(range(1, 10, 2)))
print(list(range(20, 10, -2)))

# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# range(0, 10)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# range(1, 10, 2)
# [1, 3, 5, 7, 9]
# [20, 18, 16, 14, 12]

###### Lists ######

a = ['food', 'bus', 'apple', 'queen']
print(a)
# ['food', 'bus', 'apple', 'queen']


mylist = [10, "India", "world", 8]
# accessing elements in list.
print(mylist[1])
# India

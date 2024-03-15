######### Mutable ####
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

######### Other operators ####
a = ['data', 'structures', 'using', 'python', 'happy', 'learning']
print('data' in a)
# True

print(a)
# ['data', 'structures', 'using', 'python', 'happy', 'learning']

a + ['New', 'elements']
print(a)
# ['data', 'structures', 'using', 'python', 'happy', 'learning', 'New', 'elements']

print(a * 2)
# ['data', 'structures', 'using', 'python', 'happy', 'learning', 'New', 'elements', 'data', 'structures', 'using', 'python', 'happy', 'learning', 'New', 'elements']

print(len(a))
# 6
print(min(a))

############ Membership operators

# using 'in' operator
mylist1 = [100, 20, 30, 40]
mylist2 = [10, 50, 60, 90]
if mylist1[1] in mylist2:
    print("elements are overlapping")
else:
    print("elements are not overlapping")

# Output:
# elements are not overlapping

############## SETS #############

x1 = set(['and', 'python', 'data', 'structure'])
print(x1)
# {'and', 'python', 'data', 'structure'}
print(type(x1))
# <class 'set'>

x2 = {'and', 'python', 'data', 'structure'}
print(x2)
# {'and', 'python', 'data', 'structure'}
x = {'data', 'structure', 'and', 'python'}
print(len(x))
# 4
print('structure' in x)
# True
x1 = {'data', 'structure'}
x2 = {'python', 'java', 'c', 'data'}

######### Union of two sets, x1 and x2.
x3 = x1 | x2
print(x3)
{'java', 'structure', 'c', 'python', 'data'}

print(x1.union(x2))
{'java', 'structure', 'c', 'python', 'data'}

########## Intersection of sets
print(x1.intersection(x2))
# {'data'}
print(x1 & x2)
# {'data'}

########## Difference of sets

print(x1.difference(x2))
# {'structure'}
print(x1 - x2)
# {'structure'}

######### Symmetric difference ##########
print(x1.symmetric_difference(x2))
# {'structure', 'python', 'c', 'java'}

print(x1 ^ x2)
# {'structure', 'python', 'c', 'java'}

####### subset ######

print(x1.issubset(x2))
# False
print(x1 <= x2)
# False

########## Immutable Sets #########

x = frozenset(['data', 'structure', 'and', 'python'])
print(x)
# frozenset({'and', 'python', 'data', 'structure'})
##### Error in the below code ####
'''
a11 = set(['data'])
a21 = set(['structure'])
a31 = set(['python'])
x1 = {a11, a21, a31}
'''

a1 = frozenset(['data'])
a2 = frozenset(['structure'])
a3 = frozenset(['python'])
x = {a1, a2, a3}
print(x)

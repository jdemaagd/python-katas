my_dict = {
    '1': 'Data',
    '2': 'Structure',
    '3': 'python',
    '4': 'programming',
    '5': 'language'
}

person = {}
print(type(person))
# <class 'dict'>

person['name'] = 'ABC'
person['lastname'] = 'XYZ'
person['age'] = 31
person['address'] = ['Jaipur']

print(person)
# {'name': 'ABC', 'lastname': 'XYZ', 'age': 31, 'address': ['Jaipur']}

print(person['name'])
# 'ABC'

print('name' in person)
# True
print('fname' not in person)
# True
print(len(person))
# 4

mydict = {'a': 1, 'b': 2, 'c': 3}
print(mydict)
# {'a': 1, 'b': 2, 'c': 3}
mydict.clear()
print(mydict)
# {}

'''
mydict.get('b')
print(mydict)
#2
mydict.get('z')
print(mydict)
#None

print(list(mydict.items()))
#[('a', 1), ('b', 2), ('c', 3)]

print(list(mydict.keys()))
#['a', 'b', 'c']

print(list(mydict.values()))
#[1, 2, 3]

print(mydict.pop('b'))
#2
print(mydict)
#{'a': 1, 'c': 3}
mydict = {'a': 1,'b': 2,'c': 3}
print(mydict.popitem())
#('c', 3)
print(mydict)
#{'a': 1, 'b': 2}
d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'b': 200, 'd': 400}

print(d1.update(d2))
print(d1)
#{'a': 10, 'b': 200, 'c': 30, 'd': 400}
'''

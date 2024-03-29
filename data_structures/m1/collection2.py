from collections import Counter
from collections import UserString

inventory = Counter('hello')
print(inventory)
Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1})

'''
from collections import UserDict  
class MyDict(UserDict):  
    def push(self, key, value):
        raise RuntimeError("Cannot insert")

d = MyDict({'ab':1, 'bc': 2, 'cd': 3})  
d.push('b', 2)

Traceback (most recent call last):
  File "<string>", line 12, in <module>
File "<string>", line 6, in push
RuntimeError: Cannot insert
'''

'''
from collections import UserList  
class MyList(UserList):  
    def push(self, key):
       raise RuntimeError("Cannot insert in the list")

d = MyList([11, 12, 13])  
d.push(2)

Traceback (most recent call last):
  Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in push
RuntimeError: Cannot insert in the list
'''


# create a custom append function for string
class MyString(UserString):
    def append(self, value):
        self.data += value


s1 = MyString("data")
print("Original:", s1)
# Original:  data

s1.append('h')
print("After append: ", s1)
# After append: datah

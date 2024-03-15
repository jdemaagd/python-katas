######## Named Tuples ########

from collections import namedtuple

Book = namedtuple('Book', ['name', 'ISBN', 'quantity'])
Book1 = Book('Hands on Data Structures', '9781788995573', '50')
# Accessing data items
print('Using index ISBN:' + Book1[1])
# Using index ISBN: 9781788995573
print('Using key ISBN:' + Book1.ISBN)
# Using key ISBN: 9781788995573

######## Deque ############

from collections import deque

s = deque()  # Creates an empty deque
print(s)
my_queue = deque([1, 2, 'Name'])
print(my_queue)
# deque([1, 2, 'Name'])
my_queue.append('age')
print(my_queue)
my_queue.appendleft('age')
print(my_queue)
my_queue.pop()
print(my_queue)
my_queue.popleft()
print(my_queue)

########## Ordered Dictionaries ########

from collections import OrderedDict

od = OrderedDict({'my': 2, 'name ': 4, 'is': 2, 'Mohan': 5})
od['hello'] = 4
print(od)
# ([('my', 2), ('name', 4), ('is', 2), ('Mohan', 5), ('hello', 4)])


############ Default Dictionary ########

from collections import defaultdict

dd = defaultdict(int)
words = str.split('data python data data structure data python')
for word in words:
    dd[word] += 1

print(dd)
# defaultdict(<type 'int'>, {'data': 4, 'python': 2, 'structure': 1})

############ ChainMap Object ##############

from collections import ChainMap

dict1 = {"data": 1, "structure": 2}
dict2 = {"python": 3, "language": 4}
chain = ChainMap(dict1, dict2)

print(chain)
# ChainMap({'data': 1, 'structure': 2}, {'python': 3, 'language': 4})
print(list(chain.keys()))
# ['python', 'language', 'data', 'structure']
print(list(chain.values()))
# [3, 4, 1, 2]
print(chain["data"])
# 1
print(chain["language"])
# 4

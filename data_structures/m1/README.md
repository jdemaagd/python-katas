## Overview of data types and objects

## Principal built-in types

- Numeric types: Integer (int), float, complex
- Boolean types: bool
- Sequence types: String (str), range, list, tuple
- Mapping types: dictionary (dict)
- Set types: set, frozenset

## Basic data types

- Numeric
    - Integer (int): interpreter takes sequence of decimal digits as a decimal value, such as integers 45, 1000, or -25
    - Float: considers a value having a floating-point value as a float type; it is specified with a decimal point, used
      to store floating-point numbers such as 2.5 and 100.98, accurate up to 15 decimal points
    - Complex: represented using two floating-point values, contains an ordered pair, such as a + *i*b, a and b denote
      real numbers and *i* denotes imaginary component, complex numbers take the form of 3.0 + 1.3i, 4.0i, and so on
- Boolean: provides a value of either True or False, checking whether any statement is true or false, True can be
  represented by any non-zero value, whereas False can be represented by 0
- Sequence: data types are used to store multiple values in a single variable in an organized and efficient way, there
  are four basic sequence types: string, range, lists, and tuples
    - string: immutable sequence of characters represented in single, double, or triple quotes
    - range: data type represents an immutable sequence of numbers
    - lists: used to store multiple items in a single variable
    - tuples:

## Complex data types

- mapping data types
    - dictionary: unordered {key-value} pairs; a key must be of a hashable and immutable data type, and value can be any
      arbitrary Python object
    - set: unordered collection of hashable objects, iterable, mutable, and has unique elements
    - frozenset: immutable set

## Python's collections module

- collections module provides different types of containers, which are objects that are used to store different objects
  and provide a way to access them
- namedtuple: creates a tuple with named fields similar to regular tuples
- deque: doubly-linked lists that provide efficient adding and removing of items from both ends of the list
- defaultdict: dictionary subclass that returns default values for missing keys
- ChainMap: dictionary that merges multiple dictionaries
- Counter: dictionary that returns the counts corresponding to their objects/key
- UserDict | UserList | UserString: data types are used to add more functionalities to their base data structure, such
  as a dictionary, list, and string; we can create subclasses from them for custom dict/list/string
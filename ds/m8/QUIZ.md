# Exercises

## Question 1

```
There is a hash table with 40 slots and there are 200 elements stored in the table. 
What will be the load factor of the hash table?

Solution
(# elements) / (# table slots) = 200 / 40 = 5
```

## Question 2

```
What is the worst-case search time of hashing using a separate chaining algorithm?

Solution
O(n) -> worst case being all elements being added to index 1 in a linked list
Search would than be a linear search through the list (every element)
```

## Question 3

```
Assume a uniform distribution of keys in the hash table. 
What will be the time complexities for the Search/Insert/Delete operations?

Solution
Uniform distribution means index of hash table is computed from key in O(1) time
Create -> O(n)
With uniform distribution ...
    Search | Insert | Delete -> O(1)
```

## Question 4

```
What will be the worst-case complexity for removing duplicate characters from an array of characters?

Solution
Brute Force time complexity -> O(n^2)
Run linear search to find matching character
Replace with current character and decrement length of string
Repeat until all characters are processed
```

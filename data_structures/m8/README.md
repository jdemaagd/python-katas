# Hash Tables

## Hashing methods and hash table techniques

## Different collision resolution techniques in hash tables

- Open addressing
    - Linear probing
        - drawback: clusters of consecutive occupied slots (portion may become dense)
    - Quadratic probing
        - Initially, with empty table, when we get a key element of 15 (assuming it is a hash of given string), we
          compute hash value using given hash function -> 15 mod 7 = 1. So, data element is stored at index position 1.
        - Then, let's say we get key element of 22 (assuming hash of next given string), we use hash function to compute
          hash value -> 22 mod 7 = 1, gives index position 1. We have collision at index position 1, so compute new hash
          value using quadratic probing -> 1 + 12 = 2. Index position is 2. Data element is stored at index position 2.
        - Next, assuming a data element of 29 (assuming hash of given string), compute hash value 29 mod 7 = 1. Since we
          have a collision here, we compute hash value again as in step 2, but we get another collision here, so we have
          to recompute hash value once more, in other words (1 + 22 = 5), so data is stored at that location.
        - drawback: secondary clustering creates long run of filled slots since data elements that have same hash value
          will also have same probe sequence
    - Double hashing
        - primary hash function is used to compute index position in hash table
        - another hash function to decide next free slot to store data by incrementing hashing value if a collision
        - probing interval depends on key data itself, meaning that we always map to different index positions in hash
          table whenever we get collision, which helps in avoiding formation of clusters
- Separate chaining
    - drawback: becomes inefficient when a list grows at a particular hash value location
    - worst-case time complexity for searching in a separate chaining algorithm using linked lists is O(n)
    - option for BST over linked list will get faster search and retrieval
    - does not have problem of clustering, but may become slower when all data records are hashed to a very few index
      positions in hash table

## Symbol Tables

- Used by compilers and interpreters to keep track of symbols and different entities, such as objects, classes,
  variables, and function names
- Often built using hash tables since it is important to efficiently retrieve a symbol from the table

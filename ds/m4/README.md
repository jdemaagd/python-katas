# Linked Lists

## Arrays

- Stored in contiguous memory locations
- Faster to compute position of any element in array using offset and base address (read)
- Base address refers to address of memory location where first element is stored
- Offset refers to an integer indicating displacement between first element and a given element
- Static size needs to be declared at time of creation
- Insertion and deletion operations in array data structures are slow
- Suitable when we want to do a lot of accessing of elements and fewer insertion and deletion operations

## Introducing linked lists

- Data elements are stored in memory in different locations that are connected through pointers
- Length of list can increase or decrease during execution of program
- Suitable in applications where size of list is not fixed
- Also, where a lot of insertion and deletion operations will be required vs lookups

## Singly linked lists

- Node containing data and a pointer links to next node
- The link of last node in list is None, which indicates end of list

## Doubly linked lists

- Each node contains data and two pointers, one to previous node and one to next node

## Circular lists

- Can be based on singly or doubly linked lists

## Practical applications of linked lists

- Singly linked lists
    - represent any sparse matrix
    - represent and manipulate polynomials by accumulating constants in node of linked lists
    - implementing dynamic memory management scheme that allows user to allocate and deallocate memory as per
      requirements during execution of programs
- Doubly linked lists
    - used by thread schedular in operating system to maintain list of processes running at that time
    - lists are also used in implementation of MRU and LRU cache in OS
    - can also be used by various applications to implement Undo and Redo functionality
    - browsers can implement backward and forward navigation of web pages visited
- Circular linked lists
    - can be used by operating systems to implement a round-robin scheduling mechanism
    - implement Undo functionality in Photoshop or Word software
    - implementing a browser cache that allows you to hit the BACK button
    - used to implement advanced data structures such as Fibonacci heap
    - multiplayer games also use circular linked list to swap between players in a loop

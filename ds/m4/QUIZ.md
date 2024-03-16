# Exercises

## Exercise 1

```
What will be the time complexity when inserting a data element after an element 
that is being pointed to by a pointer in a linked list?

Solution
It will be O(1), since there is no need to traverse the list to reach the desired 
location where a new element is to be added. A pointer is pointing to the current location, 
and a new element can be directly added by linking it.
```

## Exercise 2

```
What will be the time complexity when ascertaining the length of the given linked list?

Solution
O(n)
```

## Exercise 3

```
What will be the worst-case time complexity for searching a given element in a singly linked list of length n?

Solution
In the worst case, the data element to be searched will be at the end of the list, 
or will not be present in the list. In that case, there will be a total n number of comparisons, 
thus making the worst-case time complexity O(n).
```

## Exercise 4

```
For a given linked list, assuming it has only one head pointer that points to the starting point of the list, 
what will be the time complexity for the following operations?
a. Insertion at the front of the linked list
b. Insertion at the end of the linked list
c. Deletion of the front node of the linked list
d. Deletion of the last node of the linked list

Solution
a. O(1) -> operation can be performed directly through head node
b. O(n) -> requires traversing list to reach end of list
c. O(1) -> operation can be performed directly through head node
d. O(n) -> requires traversing list to reach end of list
```

## Exercise 5

```
Find the nth node from the end of a linked list.

Solution
To find the nth node from end of linked list, use two pointers, first and second. 
Move second pointer to n nodes from starting point. 
Then, move both pointers one step at a time until second pointer reaches end of list.
First pointer will be pointing nth node from end of list.
```

## Exercise 6

```
How can you establish whether there is a loop (or circle) in a given linked list?

Solution
To find out if a loop exists in a linked list, 
it is most efficient to use Floyd’s cycle-finding algorithm. 
In this approach, two pointers are used to detect the loop – 
let’s say the first and second pointers.
We start moving both the pointers from the starting point of the list.
```

## Exercise 7

```
How can you ascertain the middle element of the linked list?

Solution
It can be done with two pointers. 
First pointer should move one node at a time.
Second pointer should move 2 nodes at a time.
When second node reaches end of list, 
first node will be pointing to middle element of singly linked list.
```

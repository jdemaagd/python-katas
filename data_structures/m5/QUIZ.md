# Exercises

## Question 1

```
Which of the following options is a true queue implementation using linked lists?
a. If, in the enqueue operation, new data elements are added at the start of the list,
   then the dequeue operation must be performed from the end.
b. If, in the enqueue operation, new data elements are added to the end of the list,
   then the enqueue operation must be performed from the start of the list.
c. Both of the above.
d. None of the above.

Solution
Option b: The queue data structure follows a FIFO order, 
hence data elements must be added to the end of the list, 
and then removed from the front.
```

## Question 2

```
Assume a queue is implemented using a singly-linked list that has head and tail pointers.
The enqueue operation is implemented at the head, and the dequeue operation is implemented at the tail of the queue. 
What will be the time complexity of the enqueue and dequeue operations?

Solution
The time complexity of the enqueue operation will be O(1) and O(n) for the dequeue operation.
As for the enqueue operation, we only need to delete the head node, 
which can be achieved in O(1) for a singly linked list. 
For the dequeue operation, to delete the tail, 
we need to traverse the whole list first to the tail, and then we can delete it. 
For this we need linear, O(n), time.
```

## Question 3

```
What is the minimum number of stacks required to implement a queue?

Solution
Two stacks.
Using two stacks and the enqueue operation, the new element is entered at the top of stack1. 
In the dequeue process, if stack2 is empty, all the elements are moved to stack2, and finally, 
the top of stack2 is returned.
```

## Question 4

```
The enqueue and dequeue operations in a queue are implemented efficiently using an array. 
What will be the time complexity for both of these operations?

Solution
O(1) for both operations.
If we use a circular array for the implementation of a queue, 
then we do not need to shift the elements, just the pointers, 
so we can implement both the enqueue and dequeue operations in O(1) time.
```

## Question 5

```
How can we print the data elements of a queue data structure in reverse order?

Solution
Make an empty stack, then enqueue each of the elements from the queue and push them into the stack. 
After the queue is empty, start popping out the elements from the stack and then printing them one by one.
```

# Exercises

## Exercise 1

```
Which of the following options will be correct when a top-down approach of dynamic programming will be applied to solve 
a given problem related to the space and time complexity?

a. It will increase both time and space complexity.
b. It will increase the time complexity, and decrease the space complexity
c. It will increase the space complexity, and decrease the time complexity
d. It will decrease both time and space complexities.

Solution: option c
Since top-down approach of dynamic programming uses memoization technique, 
which stores pre-calculated solution of a subproblem. 
It avoids recalculation of same subproblem that decreases time complexity, 
but at same time, space complexity will increase because of storing extra solutions of subproblems.
```

## Exercise 2

```
Dijkstra’s single shortest path algorithm is applied on edge weighted directed graph shown in Figure 3.17. 
What will be the order of the nodes for the shortest path distance path (Assume A as source)?

A, B, C, F, E, D
In Dijkstra’s algorithm, at each, point we choose the smallest weight edge, 
which starts from any one of the vertices in the shortest path found so far, 
and add it to the shortest path.
```

## Exercise 3

```
Consider the weights and values of the items listed in Table 3.8. 
Note that there is only one unit of each item.

Item	Weight	Value
A	    2	    10
B	    10	    8
C	    4	    5
D	    7	    6

We need to maximize the value; the maximum weight should be 11 kg. 
No item may be split. 
Establish the values of the items using a greedy approach.

Solution
Firstly, we picked item A (weight 2 kg) as the value is the maximum (10). 
The second highest value is for item B, but as the total weight becomes 12 kg, 
this violates the given condition, so we cannot pick it. 
The next highest value is item D, and now the total weight becomes 2+7 = 9 kg (item A + item D). 
The next remaining item, C, cannot be picked because after adding it, 
the total weight condition will be violated.
So, the total value of the items picked up using the greedy approach = 10 + 6 = 16
```

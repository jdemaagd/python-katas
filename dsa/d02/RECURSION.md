# Recursion

## Basics

- Foundation for many algorithms such as backtracking, dynamic programming, greedy, divide & conquer
- Function calling itself until a base or terminating condition is met
- Use Cases: can problem be divided into smaller sub-problems and can solving sub-problem(s) help in
  solving original problem

## Recursive Leap of Faith

- Understand the problem -> print 3 2 1 1 2 3
- Identify the sub-problem -> print 2 1 1 2
- Trust & Faith -> trust recursive call will correctly solve smaller version of the problem
- Link original problem & sub-problem -> 3 `2 1 1 2` 3
- Base condition -> for 0, return

## Recursion Tree/Call Stack

- Memory has to be allocated for each function call
    - local variables
    - function arguments
    - return address

## Iteration

- Space complexity is better than recursion as it does not use space on the call stack
- Only has an ascending phase, no descending phase as in recursion

## Base Condition

- Last valid input -> if n is 1, return 1
- First invalid input -> if n < 1, return

## Recurrence Relation

- Expresses solution of a problem as a function of smaller instances of the same problem
- Factorial -> f(n) = n * f(n - 1)
- Fibonacci -> f(n) = f(n - 1) + f(n - 2)
- Tower of Hanoi -> f(n) = 2 * f(n - 1) + 1
- Josephus -> f(n, k) = (f(n - 1, k) + k - 1) % n + 1
- k-th symbol in Grammar -> f(n, k) = f(n - 1, (k + 1) / 2)

## Complexity Analysis

- Time complexity -> count of nodes * work done per node
    - (leaf nodes * work done per leaf node) + (non-leaf nodes * work done per non-leaf node)
- Space complexity -> depth of recursion tree

## k-th symbol in Grammar

- We build a table of `n` rows (1-indexed).
- We start by writing 0 in the 1st row.
- Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01,
  and each occurrence of 1 with 10.
- For example, for n = 3, the 1st row is 0, the 2nd row is 01, and the 3rd row is 0110.
- Given two integer n and k, return the kth (1-indexed) symbol in the nth row of a table of n rows.

## Josephus problem

- There are n friends that are playing a game.
- The friends are sitting in a circle and are numbered from 1 to n in clockwise order.
- More formally, moving clockwise from the ith friend brings you to the (i+1)th friend for 1 <= i <
  n, and moving clockwise from the nth friend brings you to the 1st friend.
- The rules of the game are as follows:
    - Start at the 1st friend.
    - Count the next k friends in the clockwise direction including the friend you started at. The
      counting wraps around the circle and may count some friends more than once.
    - The last friend you counted leaves the circle and loses the game.
    - If there is still more than one friend in the circle, go back to step 2 starting from the
      friend immediately clockwise of the friend who just lost and repeat.
    - Else, the last friend in the circle wins the game.
- Given the number of friends, n, and an integer k, return the winner of the game.

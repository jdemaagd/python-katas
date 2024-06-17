"""
There are n friends that are playing a game.
The friends are sitting in a circle and are numbered from 1 to n in clockwise order.
More formally, moving clockwise from the ith friend brings you to the (i+1)th friend for 1 <= i < n,
  and moving clockwise from the nth friend brings you to the 1st friend.
The rules of the game are as follows:
    Start at the 1st friend.
    Count the next k friends in the clockwise direction including the friend you started at.
      The counting wraps around the circle and may count some friends more than once.
    The last friend you counted leaves the circle and loses the game.
    If there is still more than one friend in the circle, go back to step 2 starting from the
      friend immediately clockwise of the friend who just lost and repeat.
    Else, the last friend in the circle wins the game.
Given the number of friends, n, and an integer k, return the winner of the game.
"""


# Time Complexity: O(n^2)
# Space complexity: O(n)
def approach1(n, k):
    arr = [i + 1 for i in range(n)]

    def helper(arr1, start_index):
        if len(arr1) == 1:
            return arr1[0]
        index_to_remove = (start_index + k - 1) % len(arr1)
        del arr1[index_to_remove]
        return helper(arr1, index_to_remove)

    return helper(arr, 0)


# Time Complexity: O(n)
# Space complexity: O(n)
def approach2(n, k):    # using solution to sub-problem to solve original problem
    def josephus(n1):
        if n1 == 1:
            return 0
        return (josephus(n1 - 1) + k) % n1

    return josephus(n) + 1


# Time Complexity: O(n)
# Space complexity: O(1)
def approach3(n, k):    # improve space complexity of recursive call stack
    survivor = 0
    for i in range(2, n + 1):
        survivor = (survivor + k) % i

    return survivor + 1


print(approach3(5, 2))  # 3
print(approach3(6, 5))  # 1

"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
Given an integer n, return all distinct solutions to the n-queens puzzle.
You may return the answer in any order.
Each solution contains a distinct board configuration of the n-queens' placement,
where 'Q' and '.' both indicate a queen and an empty space, respectively.

Example 1
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

Example 2
Input: n = 1
Output: [["Q"]]

Constraints:
    1 <= n <= 9

Observations:
1. only one queen per row
"""


# Time Complexity: O(n!)
#   row 1 -> n, row 2 -> n - 2, row 3 -> n - 4, etc.
#   roughly -> n!, not O(n^n) because of pruning
# Space Complexity: O(n^2), hold state of board -> n x n = n^2
#   recursive call stack will take order of n, we take n^2 as the dominating factor
def solve_n_queens(n):
    res = []
    # board is a list of lists
    # we will convert this to a list of strings when we append to results
    board = [['.'] * n for _ in range(n)]

    def convert_board(board1):
        # creates a new list, different from the original board list of lists
        return [''.join(row) for row in board1]

    # checking row by row so only need to check col and top left/right diagonals
    def is_valid(row, col, board1):
        for x in range(row):        # check col up to this row
            if board1[x][col] == 'Q':
                return False

        # top left diagonal
        for r, c in zip(range(row, -1, -1), range(col, -1, -1)):
            if board1[r][c] == 'Q':
                return False

        # top right diagonal
        for r, c in zip(range(row, -1, -1), range(col, n, +1)):
            if board1[r][c] == 'Q':
                return False

        return True

    def position_next_queen(board1, row):
        # base case
        if row == n:
            res.append(convert_board(board1))
            return
        for col in range(n):
            if is_valid(row, col, board1):
                board1[row][col] = 'Q'
                position_next_queen(board1, row + 1)
                board1[row][col] = '.'                  # backtracking step

    position_next_queen(board, 0)

    return res


print(solve_n_queens(4))
print(solve_n_queens(1))

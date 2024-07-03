"""
Write a program to solve a Sudoku puzzle by filling the empty cells.
A sudoku solution must satisfy all the following rules:
    Each of the digits 1-9 must occur exactly once in each row.
    Each of the digits 1-9 must occur exactly once in each column.
    Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.

Example -> see example.png

Constraints:
    board.length == 9
    board[i].length == 9
    board[i][j] is a digit or '.'.
    It is guaranteed that the input board has only one solution.
"""


# Time Complexity: O(1), as board size is fixed
#     operations bound by 9^(# of empty cells), max 9^81
# Space Complexity: O(1), no n to track
#     max depth of recursion stack can be at most 81
def solve_sudoku(board):
    # function modifies board in place, hence there is no need to return the board

    def is_valid(row, col, num):
        for x in range(9):
            # check row and column
            if board[x][col] == num or board[row][x] == num:
                return False

            # calculations to see board in a 3 x 3 sub-grid
            r = 3 * (row // 3) + x // 3
            c = 3 * (col // 3) + x % 3
            if board[r][c] == num:
                return False

        return True     # valid `num`

    def fill_board():
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':                  # identify next empty cell
                    for num in '123456789':
                        if is_valid(row, col, num):
                            board[row][col] = num           # choose step
                            if fill_board():
                                return True
                            board[row][col] = '.'           # backtracking step

                    return False    # need to backtrack no numbers (1 - 9) were valid

        return True    # valid sudoku board

    fill_board()

    return board


print(solve_sudoku([
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]))

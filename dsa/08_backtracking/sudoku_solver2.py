def solve_sudoku2(board):
    """
    Do not return anything, modify board in-place instead.
    """
    boxes1 = [{} for _ in range(9)]
    rows1 = [{} for _ in range(9)]
    cols1 = [{} for _ in range(9)]

    def get_box(row, col):
        new_c = col // 3
        new_r = (row // 3) * 3
        return new_c + new_r

    for i in range(9):
        for j in range(9):
            if board[i][j] != '.':
                value = board[i][j]
                x = get_box(i, j)
                boxes1[x][value] = True
                rows1[i][value] = True
                cols1[j][value] = True

    def is_valid2(box, row, col, num):
        if (num in box) or (num in row) or (num in col):
            return False
        return True

    def backtrack(boxes, rows, cols, r, c):
        if r == 9:
            return True
        if board[r][c] == '.':
            box = get_box(r, c)
            for num in range(1, 10):
                numVal = str(num)
                boxId = get_box(r, c)
                box = boxes[boxId]
                row = rows[r]
                col = cols[c]
                if is_valid2(box, row, col, numVal):
                    board[r][c] = numVal
                    box[numVal] = True
                    row[numVal] = True
                    col[numVal] = True
                    if c == 8:
                        if backtrack(boxes, rows, cols, r + 1, 0):
                            return True
                    else:
                        if backtrack(boxes, rows, cols, r, c + 1):
                            return True
                        # backtrack
                    del box[numVal]
                    del row[numVal]
                    del col[numVal]
                    board[r][c] = '.'
            return False
        else:
            if c == 8:
                if backtrack(boxes, rows, cols, r + 1, 0):
                    return True
            else:
                if backtrack(boxes, rows, cols, r, c + 1):
                    return True

    backtrack(boxes1, rows1, cols1, 0, 0)

    return board


print(solve_sudoku2([
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

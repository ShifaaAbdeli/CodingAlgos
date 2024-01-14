class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        1- Collect each row's chars and add them to a row set
        2- Collect each col's chars and add them in a col set
        3- Collect each sub-boxes' chars and add them to a sub-boxes set
        4- Parse all board and make sure no element [r][c] is repeted in
           the above set(s). Else Sudoku is valid
        """
        ROWS = len(board)
        COLS = len(board[0])
        rows_chars = [set() for _ in range(ROWS)]
        cols_chars = [set() for _ in range(COLS)]
        squares_chars = [set() for _ in range(ROWS)]

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows_chars[r] or
                    board[r][c] in cols_chars[c] or
                    board[r][c] in squares_chars[(r//3) * 3 + c//3]):
                    return False

                rows_chars[r].add(board[r][c])
                cols_chars[c].add(board[r][c])
                squares_chars[(r//3) * 3 + c//3].add(board[r][c])

        return True
    #### Time complexity O(n2) since we traverse the each element once and
    #### space O(n2) because of 3 hash set.
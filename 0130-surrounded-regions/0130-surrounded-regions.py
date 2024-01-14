class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def bfs(board, row, col):            
            queue = deque([(row, col)])
            while queue:
                (row, col) = queue.popleft() #pop from the head for Queue, BFS
                # (r, c) = queue.pop() # pop from the tail for the Stack, DFS
                if board[row][col] != 'O':
                    continue
                # make this cell as escaped
                board[row][col] = 'E'
                # put (row, col) cells neigbor to queue
                if col > 0: 
                    queue.append((row, col - 1))
                if col < COLS - 1:
                    queue.append((row, col + 1))
                if row > 0:
                    queue.append((row - 1, col))
                if row < ROWS - 1:
                    queue.append((row + 1, col))

        if not board or not board[0]:
            return

        ROWS = len(board)
        COLS = len(board[0])

        # Compute the borders of the board
        borders = list(product(range(ROWS), [0, COLS - 1])) + list(product([0, ROWS - 1], range(COLS)))
        # We loop in this borderds list and we 
        # Set 'O' to a placeholder 'E'
        for row, col in borders:
            bfs(board, row, col)
        
        # Flip the remaining 'O' in the board to 'X' and
        # flip the placeholder 'E' of the borders to 'X'
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'E':
                    board[r][c] = 'O'
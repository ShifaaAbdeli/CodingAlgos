class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ### Using BFS approach.
        ### 1- count the Fresh oranges
        ### 2- queue the rotten oranges
        ### 3- For every queue elements processing 
        ### count 1 unit time.

        ROWS, COLS = len(grid), len(grid[0])
        direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        queue = deque()
        fresh = 0
        time = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append((r,c))

        while fresh > 0 and queue:
            lenght = len(queue)
            # Every length of the current queue size 
            # is one time unit
            for i in range(lenght):
                row, col = queue.popleft()
                # Process every direction of 4 directions.
                # make rotten teach neigbhor orange
                for dr, dc in direction:
                    if row+dr in range(ROWS) and col+dc in range(COLS) and grid[row+dr][col+dc] == 1:
                        grid[row+dr][col+dc] = 2
                        queue.append((row+dr, col+dc))
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1

        ### Time complexity O(m*n), Space O(m*n)
        



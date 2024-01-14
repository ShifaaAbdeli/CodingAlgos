class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:


    #    ROWS = len(grid)
    #    COLS = len(grid[0])
    #    visited = set()

    #    def dfs(r, c):
    #        if (r < 0 or c < 0 or r == ROWS or c == COLS or grid[r][c] == 0 or (r, c) in visited):
    #            return 0
    #        visited.add((r, c))
    #        return (1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1))

    #    maxArea = 0
    #    for r in range(ROWS):
    #        for c in range(COLS):
    #            maxArea = max(maxArea, dfs(r, c))
    #    return maxArea

    ### Time complexity is O(m*n), space O(m*n)

        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        maxIslands = 0
        lands = 0

        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            visit.add((r, c))
            direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            curLand = 1
            while queue:
                row, col = queue.popleft()
                for dr, dc in direction:
                    r = row + dr
                    c = col + dc
                    if r in range(ROWS) and c in range(COLS) and grid[r][c] == 1 and (r, c) not in visit:
                        queue.append((r,c))
                        visit.add((r, c))
                        curLand += 1
            return curLand

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visit:
                    lands = bfs(r,c)
                    maxIslands = max(maxIslands, lands)

        return maxIslands
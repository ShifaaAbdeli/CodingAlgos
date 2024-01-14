class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        #def dfs(grid, r, c) :
        #    numberRaw = len(grid)
        #    numberCol = len(grid[0])

        #    grid[r][c] = 0
        #    if r-1 >= 0 and grid[r-1][c] == '1':
        #        dfs(grid, r-1, c)
        #    if r+1 < numberRaw and grid[r+1][c] == '1':
        #        dfs(grid, r+1, c)
        #    if c-1 >= 0 and grid[r][c-1] == '1':
        #        dfs(grid,r,c-1)
        #    if c+1 < numberCol and grid[r][c+1] == '1':
        #        dfs(grid, r, c+1)

        #numberRaw = len(grid)
        #if numberRaw == 0:
        #    return 0
        #numberCol = len(grid[0])

        #numberIsland = 0
        #for raw in range(numberRaw):
        #    for col in range(numberCol):
        #        if grid[raw][col] == "1":
        #            dfs(grid, raw, col)
        #            numberIsland += 1

        #return numberIsland
        # Time complexity is O(n+m) and worst Space complexity is O(n+m)
        if grid is None:
            return

        ROWS = len(grid)
        COLS = len(grid[0])
        # need to mark the visited grid element (r,c)
        visited = set()
        islands = 0

        # bfs to traverse the grid for islands
        def bfs(r,c):
            queue = deque()
            queue.append((r,c))
            visited.add((r,c))
            while queue:
                ### To do a DFS traversal i=just replace popleft with pop ###
                (row, col) = queue.popleft()
                # The code that address the grid island requirement
                gridDirection = [[-1, 0], [1,0], [0, -1], [0, 1]]
                for dr, dc in gridDirection:
                    r, c = row + dr, col + dc
                    if r in range(ROWS) and c in range(COLS) and grid[r][c] == "1" and (r,c) not in visited:
                        # queuing the next grid element that is "1" and 
                        # set it as visited
                        queue.append((r, c))
                        visited.add((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands += 1
        return islands

        ### The time complexity O(mxn) and space is O(mxn)


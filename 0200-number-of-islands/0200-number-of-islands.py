class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # base case
        if not grid or not grid[0]:
            return 0
        
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        visit = set()
        
        # DFS function
        def dfs(r, c):
            if min(r,c) < 0 or r == ROWS or c == COLS or (r, c) in visit or grid[r][c] == "0":
                return
            visit.add((r,c))
            directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        
        # main code for numIslands
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visit:
                    islands += 1
                    dfs(r, c)
        return islands
    
    ## Time compexity: O(4^N*M),  Space: O(N*M)
                
            
        
        
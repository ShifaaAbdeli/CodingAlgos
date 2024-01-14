class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        #### DP approach ####
        # 1- need to use an array [len(grid)] where 
        #    to store the paths number
        # 2- if the grid[r][c] obstacle, set grid[r][c] == 0
        # 3- elif c + 1 < len(grid), update the dp array 
        #     position for a c colon position
        # 4- when all loops over the grid is over return the dp[0]
        ####

        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])
        dp = [0] * COLS
        dp[COLS-1] = 1

        for r in reversed(range(ROWS)):
            for c in reversed(range(COLS)):
                if obstacleGrid[r][c]:
                    dp[c] = 0
                elif c + 1 < COLS:
                    # dp[c] is the previouse value of 
                    # previouse row r and same colon 
                    dp[c] = dp[c] + dp[c + 1]
        return dp[0]

        ### Time complexity O(m*n) and space is O(n)
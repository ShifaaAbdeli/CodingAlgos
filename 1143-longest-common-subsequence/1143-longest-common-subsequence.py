class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #### DP approach ####
        # 1- create a 2D matrix with text1 and text2.
        # 2- compare the text1 and text2 elements and 
        #    populate the 2D matrix starting from bottom Up of 2D.
        #    Add 1 + the dayagonal value 
        # 3- When matching, add 1 to the dayagonal value of i, j
        # 4- else, take the max of dp[i+1][j] and dp[i][j+1]
        #####
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

        for i in reversed(range(len(text1))):
            for j in reversed(range(len(text2))):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])

        return dp[0][0]

        #### Time complexity O(m*n), space O(m*n)
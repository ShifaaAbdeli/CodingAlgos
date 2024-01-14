class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #### DP approach ####
        # 1- intialize bottow first row 0 to 1s
        # 2- at ith newRow in m-1 rows, start from
        #    right end of newRow n-2, since n-1 are
        #    all set to 1).
        # 3-  newRow[j] = newRow[j+1] + row[j] ###


        # bottom initial row init to 1 since 
        # one path to get finish position at 
        # right side.
        bottomRow = [1] * n

        # Loop on m-2 rows, since row m-1 is 
        # set to 1s
        for i in range(m-1):
            newRow = [1] * n # It also initialize the newRow right element to 1
            for j in range(n-2, -1, -1):
                newRow[j] = newRow[j+1] + bottomRow[j]
            bottomRow = newRow
        return bottomRow[0]

        ## Time complexity O(m*n), space O(n)
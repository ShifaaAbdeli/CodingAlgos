"""
        B.F.: 
             [[1,1,1],
              [1,0,1],
              [1,1,1]]
              
        for i in range(ROW):
          for j in range(COL):
              if matrix[i][j] == 0:
                 k = 0
                 l = 0
                 while k < COL:
                    matrix[i][k] = 0
                 while l < ROW:
                    matrix[l][j] = 0
        Time complexity: O(mxnxmxn). Space: O(1)
        
        
        Improve time complexity:
        ========================
        - Loop on ROW and COL and if an element 
          is null set its first element of the 
          row to 0 and first elementb of colon to 0
          
        - Loop on ROW and COL and if fisrt elemnt of 
          ROW or COL is 0 set all ROW to colon tto 0
          
          
             [[1,1,1],
              [1,0,1],
              [1,1,1]]
              
             [[1,0,1],
              [1,0,1],
              [1,1,1]]
"""

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROW = len(matrix)
        COL = len(matrix[0])
        rowZero = False
        
        for r in range(ROW):
            for c in range(COL):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    elif r == 0:
                        rowZero = True
                    
        for r in range(1,ROW):
            for c in range(1, COL):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # Process first col, col zero          
        if matrix[0][0] == 0:
            for r in range(ROW):
                matrix[r][0] = 0
                
        # Process first row, row zero       
        if rowZero == True:
            for c in range(COL):
                matrix[0][c] = 0

        ## Time complexity: O(nxm), Space: O(1)
                    
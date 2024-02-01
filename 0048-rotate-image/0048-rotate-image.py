class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Use two pointers approach, left and right
        l, r = 0, len(matrix) - 1
        
        while l < r:
            for i in range(r - l):
                
                # need to use top and bottom
                top, bottom = l, r
                
                # Save topLeft
                topLeft = matrix[top][l + i]
                
                # move bottom left to top left
                matrix[top][l+i] = matrix[bottom - i][l]
                
                # move bottom right to bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]
                
                # move top rigth to bottom right
                matrix[bottom][r - i] = matrix[top + i][r]
                
                # move topLeft to top right
                matrix[top + i][r] = topLeft
                
            l += 1
            r -= 1
                
                
        
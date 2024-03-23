"""
1- Use binary search to find the ROW that may contain the tearget
2- use the ROW found above and use binary search to find the COL that contain the target
3- Time complexity is O(log(n)). Space is O(1)

"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        
        top, bot = 0, ROWS - 1
        while top <= bot:
            row = (top + bot) // 2
            if target < matrix[row][0]:
                bot = row - 1
            elif target > matrix[row][-1]:
                top = row + 1
            else:
                break
                
   #     if not (top <= bot):
  #          return False
        
        ## row where target is possibly located
        row = (top + bot) // 2
        ## search for possible colone for the tearget
        l, r = 0, COLS-1
        while l <= r:
            mid = (l + r)//2
            if target < matrix[row][mid]:
                r = mid -1
            elif target > matrix[row][mid]:
                l = mid + 1
            else:
                return True
        return False
            
        
        
        

        
        
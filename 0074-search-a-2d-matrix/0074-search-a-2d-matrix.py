class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        RAWs = len(matrix)
        if RAWs == 0:
            return False
        COLs = len(matrix[0])
    
        l, r = 0, COLs * RAWs - 1
        while l <= r:
            mid = l +((r - l)//2) # to avoid overflow issue
            mid_element = matrix[mid//COLs][mid % COLs]
            if target < mid_element:
                r = mid -1
            elif target > mid_element:
                l = mid + 1
            else:
                return True
        return False
### Time complexity O(nlog(n)), Space O(1)
    

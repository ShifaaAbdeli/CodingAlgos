class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Use of two pointer approach
        maxArea = 0
        l = 0
        r = len(height) - 1
        while l < r:
            # Update the maxArea with the current area 
            # or existing maxArea
            maxArea = max(maxArea, (min(height[r], height[l])*(r-l)))
            # Shift the l ptr to left 
            if height[l] < height[r]:
                l += 1
            # Shift the r ptr to right
            elif height[l] >= height[r]:
                r -= 1
        # return the final maxArea
        return maxArea


        
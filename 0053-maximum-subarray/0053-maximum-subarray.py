"""
        1- Using L and R ptrs, we loop R over nums
        2- use curSum as sum of nums[R], and use a maxSum whe 
           we keep track of maximum sum
        3- if curSum is < 0 we reset the curSum to 0 and
           we move L to R ptr
        4-  return maxSum for subarray[maxL, maxR]
"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum, maxSum = 0, nums[0]
        maxL, maxR = 0, 0
        L = 0
        for R in range(len(nums)):
            if curSum < 0:
                curSum = 0
                L = R
            curSum += nums[R]
            if curSum > maxSum:
                maxSum = curSum
                maxL, maxR = L, R
        # return [maxL, maxR] we can also retuwn the indexes [maxL, maxR]
        return maxSum

        #### Time complexity O(n), Sapce O(1)
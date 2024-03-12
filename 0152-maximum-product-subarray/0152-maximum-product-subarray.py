"""
 - nums = [2,3,-2,4]

 BF. :  
 Multiplay the subarray element from a loop on the array and keep the max
      largProd = 0
      loop x in range(len(nums)):
         loop y in range(x, len(nums) - x):
            largProd = max(largProd, nums[x]*nums[y])
      return largProd
      
      - Time Complexity: O(n^2), space: O(1)
      
 Dynamic Programming:
 - nums = [2,3,-2,4]
 
           [2]
           [2,3] 
           [2,3,-2]
           [2,3,-2,4]
           [3]
           [3,-2]
           [3,-2,4]
           [-2]
           [-2,4]
           [4]
         
    curMin, curMax = 1, 1
    n = nums[0] = 2; tempMax = curMax x n, 
        curMax = 2x1, curMin = min(tempMax, n x curMin, n) = 2
    n = nums[1] = 3; tempMax = curMax x n = 6, 
        curMax = max(curMax x n, curMin x n, n) = 6
        curMin = min(tempMax, curMin, n) = 2
 
 Second Approach:
    pre = 1
    surf = 1
    maxSubArr = INT_MIN
    for i in range(len(nums)):
        if pre == 0:
           pre = 1
        if surf == 0:
           surf = 1
           
        pre = pre * nums[i]
        suff = suff * nums[n-1-i]
        maxSubArr = max(maxSubArr, pre, suff)
        
    return maxSubArr
    
"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pref = 1
        surff = 1
        maxSubArr = min(nums)
        ARR = len(nums)
        
        for i in range(ARR):
            if pref == 0:
                pref = 1
            if surff == 0:
                surff = 1
                
            pref = pref * nums[i]
            surff = surff * nums[ARR-1-i]
            maxSubArr = max(maxSubArr, pref, surff)
            
        return maxSubArr
        
        
        
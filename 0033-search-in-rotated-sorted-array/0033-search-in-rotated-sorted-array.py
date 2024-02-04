"""
Input: nums = [4,5,6,7,0,1,2], target = 0
1- B.F. approach: loop and check for target. Time O(n), space: O(1)

2- Two ptrs:
Input: nums = [4,5,6,7,0,1,2], target = 0
               l     mid     r
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l+r) // 2
            
            if nums[mid] == target:
                return mid
            
            # left sorted part of nums
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # right sorted part of nums
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid -1 
                else:
                    l = mid + 1
            
        return -1
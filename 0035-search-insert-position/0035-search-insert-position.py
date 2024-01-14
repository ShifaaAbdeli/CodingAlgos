class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            p = (left + right)//2

            if target == nums[p]:
                return p
            if target < nums[p]:
                right = p - 1
            else:
                left = p + 1
        # Target not found, meaning that 
        # the last left position is where 
        # we suposed to insert the new element 
        # from the sorted array
        return left
        # Time complexity O(log N) (Binary Search), Space complexity O(1)

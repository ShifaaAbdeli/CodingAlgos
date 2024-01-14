class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # If next element differs by 1, 
        # we include the (i+1)th element in 
        # this range and increment i by 1.

        ranges = []
        idx = 0
        # loop on nums and use start num element 
        # as starting of ranges
        while idx < len(nums):
            startNum = nums[idx]
            # Check for conteguise integers in nums  
            while idx+1 < len(nums) and nums[idx+1] - nums[idx] ==1:
                idx += 1
            if startNum != nums[idx]:
                ranges.append(str(startNum) + "->" + str(nums[idx]))
            else:
                ranges.append(str(startNum))
            idx += 1
        return ranges

        



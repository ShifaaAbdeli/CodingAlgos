class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # val: index
        
        for idx, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [idx, prevMap[diff]]
            prevMap[n] = idx
        return
            
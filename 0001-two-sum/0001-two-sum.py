class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #mapList = {} # value, index
        #for index, value in enumerate(nums):
        #    diff = target - value
        #    if diff in mapList:
        #        return [mapList[diff], index]
        #    mapList[value] = index
        #return []


        ###### Approach HashMap {nums[index]:index} #####
        hashMapTwoSum = {}
        for index, val in enumerate(nums):
            diff = target - val
            if diff in hashMapTwoSum:
                return [index, hashMapTwoSum[diff]]
            hashMapTwoSum[val] = index
        

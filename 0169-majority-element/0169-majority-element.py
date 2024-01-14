class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
       
        return nums[len(nums)//2]
    # I was using a while loop and counting for majority element
    # I also solved it with hashmap where
    # key is num and value is index of num in nums array
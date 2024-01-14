class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        r = 0
        l = 0
        #n = len(nums)
        #while r < n: we replace it with for loop to increment r
        #for r in range(n):
        #   if nums[r] != val:
        #        # we write only the element that != val
        #        nums[w] = nums[r]
        #        w += 1
        #return w

        for r in range(len(nums)):
            if nums[r] != val:
                nums[l] = nums[r]
                l += 1
        return l
        # Time complexity O(n), space complexity O(1)


        
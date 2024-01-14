class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # use two pointer r and w technic and starting from index 1 !!
        #r = 1
        #w = 1
        #n = len(nums)
        #while r < n:
        #    if nums[r] != nums[r-1]:
        #        nums[w] = nums[r]
        #        w += 1
        #    r += 1
        #return w
        n = len(nums)
        L, R = 1, 1
        for R in range(1,n):
            if nums[R] != nums[R-1]:
                nums[L] = nums[R]
                L += 1
        return L


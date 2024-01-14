class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort()

        for i, num in enumerate(nums):

            # If num is positive break, since there is not solution
            if num > 0:
                break

            # If num of i is equal to i-1, need to skip for duplicate
            if i > 0 and num == nums[i-1]:
                continue
        
            # loop on all [l, r] list to check for the triple num
            l = i+1
            r = len(nums) - 1
            while l < r:
                sum3 = num + nums[l] + nums[r]
                if sum3 < 0:
                    l += 1
                elif sum3 > 0:
                    r -= 1
                else:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

        return res


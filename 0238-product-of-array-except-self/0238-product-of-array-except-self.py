class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        LEN = len(nums)
        L, R, answer = [0]*LEN, [0]*LEN, [0]*LEN
        L[0] = 1

        for i in range(1, LEN):
            L[i] = nums[i-1] * L[i-1]

        R = 1
        for i in range(LEN-1, -1, -1):
            L[i] = L[i] * R
            R *= nums[i]

        #for i in range(LEN):
            #answer [i] = L[i] * R[i]
        
        return L



"""
        lenght = len(nums)
        answer = [1] * lenght
        # Left product calculation
        leftProduct = 1
        for i in range(lenght):
            answer[i] = leftProduct
            leftProduct *= nums[i]

        # Right product calculation 
        rightProduct = 1
        for i in range(lenght - 1, -1, -1):
            answer[i] *= rightProduct
            rightProduct *= nums[i]

        return answer
"""
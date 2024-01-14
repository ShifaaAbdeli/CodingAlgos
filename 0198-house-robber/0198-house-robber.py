class Solution:
    def rob(self, nums: List[int]) -> int:
        #### DP approach ####
        # 1- [1,2,3,1], need to start to rob a 
        #       max money house 1 (rob1) or 2
        #       (rob2) from the nums above.
        # 2- Then next possible house to rob is
        #   house 3 (house n) to avoid the alarm. 
        # 3- To maximize the money, need to take
        #     the max of (rob1 + n, rob2) of the
        #      two possibility above
        # 4- We can return the max (we can
        #     maintined max in rob2) and return it
        #     at the end
        ###
        rob1, rob2 = 0, 0
        for n in nums:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2

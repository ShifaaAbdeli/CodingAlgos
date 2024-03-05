class Solution:
    def rob(self, nums: List[int]) -> int:
        #### DP approach ####
        # [1   , 2   , 3,  1]
        #  rob1, rob2, n, n+1, ...
        # 1- [1,2,3,1], need to start to rob a 
        #     house 1 (rob1) or house 2
        #       (rob2) from the nums above.
        # 2- Then next possible house to rob is
        #   house 3 (house n) to avoid the alarm.
        
        # 3- To maximize the money, need to take
        #     the max of (rob1 + n, rob2) of the
        #      two possibility above at (2)
        #
        # 4- next the rob1 became rob2 and rob2 became the max and return rob2
        #     at the end of the loop on nums
        ###
        rob1, rob2 = 0, 0
        for n in nums:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2

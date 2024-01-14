class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # 1- use Binary Tree (B.T) with DFS approach recursive way
        # 2- Left of B.T and at level i, will constract subset with the 
        #    next element i of the array.
        # 3- Right of B.T and at level i, will constract subset without 
        #    the element i nor its duplicat
        
        subSetsArr, curSubSet = [], []
        nums.sort()  ## Critical step to sort the nums array!!!

        def dfsHelper(i):
            if i >= len(nums):
                subSetsArr.append(curSubSet.copy())
                return
            # Left side, craete set with the num[i]
            curSubSet.append(nums[i])
            dfsHelper(i+1)

            # Right side, create the set without the num[i]
            curSubSet.pop()
            # exclude duplicate elements from nums array
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            dfsHelper(i+1)

        dfsHelper(0)
        return subSetsArr

        ## Time complexity: O(n*2^n). Space: O(n) 
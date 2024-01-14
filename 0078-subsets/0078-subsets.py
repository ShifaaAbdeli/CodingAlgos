class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsetArr = []
        subset = []
        def dfsSubset(i):
            # Base case for this DFS binary tree
            if i >= len(nums):
                subsetArr.append(subset.copy())
                return
            # Left side of DFS binary tree, where 
            # we add nums[i] at left side of dfs tree
            subset.append(nums[i])
            dfsSubset(i+1)

            # Left side of the DFS t=binary Tree:
            # not adding nums[i] to subset (pop the 
            # last nums[i] we previousely added to subset)
            subset.pop()
            dfsSubset(i+1)

        dfsSubset(0)
        return subsetArr
        
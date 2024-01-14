class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # - Iteratif approach:
        # - for each permutation in permutation list [[]]
        #   - loop over the range of len of the perm list + 1
        #   - create a copy of the perm ans insert each n element 
        #     of nums at each position i of the permu.
        #   - append the copy to the list of permutations
        #    
        
        permutations = [[]]

        for n in nums:
            nextPermut = []
            for p in permutations:
                for i in range(len(p) + 1):
                    permCopy = p.copy()
                    # insert the n in each i position of the permut (p)
                    permCopy.insert(i, n)
                    nextPermut.append(permCopy)
                # put these purmutation in permutations
                permutations = nextPermut
        
        return permutations

        ## Time complexity is mathimaticly O(n^2*n!). Space: O(n)


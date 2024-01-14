class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        arr = []
        ### DFS + backtracking approach
        # Defin a DFS for this combinationSum. 
        # It keep adding same element of candidat at 
        # the left child ONLY, until it matches the target 
        #value on that side.
        # For the right side of it will never add that 
        # same elemnt. It will  continue filling up the 
        # rest of the dfs tree with the remaining 
        # candidates (minus the elelemnt used in left side)
        def dfsCombinationSum(i, currCandidates, total):
            if total == target:
                return arr.append(currCandidates.copy())
            if i >= len(candidates) or total > target:
                return

            currCandidates.append(candidates[i])
            dfsCombinationSum(i, currCandidates, total + candidates[i])
            
            # Remove the last element we add at left side, 
            # before we compute the right side
            currCandidates.pop()

            dfsCombinationSum(i+1, currCandidates, total)

        dfsCombinationSum(0, [], 0)
        return arr

        ### Time complexity O(2^target). Space O(n)
        
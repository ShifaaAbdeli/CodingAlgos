class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        dictDup_II = {}

        for idx, val in enumerate(nums):
            if val in dictDup_II and abs(idx - dictDup_II[val]) <= k:
                return True
            dictDup_II[val] = idx
        return False
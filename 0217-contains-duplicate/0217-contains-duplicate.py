class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen_set = set()

        for num in nums:
            if num in seen_set:
                return True
            else:
                seen_set.add(num)

        return False
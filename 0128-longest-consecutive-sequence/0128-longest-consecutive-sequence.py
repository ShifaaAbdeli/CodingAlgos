class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numSet = set(nums)
        longSequence = 0

        for num in nums:
            if (num - 1) not in numSet:
                countSequence = 0
                while (num + countSequence) in numSet:
                    countSequence += 1
                longSequence = max(longSequence, countSequence)

        return longSequence
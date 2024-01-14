class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0, 0, 0]  # Assuming nums contain only 0, 1 and 2

        # Count the quantity of each value in the nums
        for n in nums:
            counts[n] += 1
        
        # Fill each bucket in the original array nums
        i = 0
        for n in range(len(counts)):
            for j in range(counts[n]):
                nums[i] = n
                i += 1
        return nums

    ### Time complexity is O(n), and space complexity is O(n)


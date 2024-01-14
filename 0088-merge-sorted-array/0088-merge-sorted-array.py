class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        for num in nums2:
            i += 1
            nums1[m -1 + i] = num
        nums1.sort()

        
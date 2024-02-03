"""
Input: n = 00000000000000000000000000001011
           

"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        return n.bit_count()
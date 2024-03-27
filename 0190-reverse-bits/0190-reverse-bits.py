"""
Input: n = 00000010100101000001111010011100
Output:    964176192 (00111001011110000010100101000000)
- loop on 32bit length (from 0 to 31)
-   shift result left by 1 
    if less sinificant bit of n is 1, we add 1 to result
    then we can shift the n right by 1 to process the next bit of n
at the end of the loop we return res

"""

class Solution:
    def reverseBits(self, n: int) -> int:
        if n == 0:
            return 0
        res = 0
        for i in range(32):
            res <<= 1
            if n & 1 == 1:
                res += 1
            n >>= 1
        return res
    
## Time complexity: O(n=32) = O(1),  Space: O(n=32) = O(1)
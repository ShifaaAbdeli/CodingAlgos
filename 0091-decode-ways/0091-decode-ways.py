class Solution:
    def numDecodings(self, s: str) -> int:
        # Define a dp array of size len(s)+1
        dp = [0 for _ in range(len(s)+1)]
        
        # Initialize dp[0] to 1 and 
        #dp[0] = 1
        twoBack = 1
        
        # dp[1] to 1 if fisrt char of s[0] is not '0'
        #dp[1] = 1 if s[0] != '0' else 0
        oneBack = 1 if s[0] != '0' else 0
        
        for i in range(1, len(s)):
            current = 0
            # Check if single digit of s is possibly succesful decoding
            if s[i] != '0':
                current = oneBack # s[i-1] is mapped to dp[i]
                
            # Check if the two digit of s is possible succesful decoding
            two_digit = int(s[i-1:i+1])
            if two_digit >= 10 and two_digit <= 26:
                current += twoBack
            twoBack = oneBack
            oneBack = current
                
        # The dp of the len(s) position and the number of possible decoding        
        return oneBack
            
 ## Time complexity: O(n), Space : O(n)           
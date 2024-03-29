class Solution:
    def numDecodings(self, s: str) -> int:
        # Define a dp array of size len(s)+1
        dp = [0 for _ in range(len(s)+1)]
        
        # Initialize dp[0] to 1 and 
        dp[0] = 1
        
        # dp[1] to 1 if fisrt char of s[0] is not '0'
        dp[1] = 1 if s[0] != '0' else 0
        
        for i in range(2, len(dp)):
            
            # Check if single digit of s is possibly succesful decoding
            if s[i-1] != '0':
                dp[i] = dp[i-1] # s[i-1] is mapped to dp[i]
                
            # Check if the two digit of s is possible succesful decoding
            two_digit = int(s[i-2:i])
            if two_digit >= 10 and two_digit <= 26:
                dp[i] += dp[i-2]
                
        # The dp of the len(s) position and the number of possible decoding        
        return dp[len(s)]
            
            
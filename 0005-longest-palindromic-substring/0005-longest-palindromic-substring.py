"""
- Use Dynamic Programming approach with two pointers:
       0   5
  s = "babad" , len(s)=5 odd ---> l=r ---> l -=1 and r +=1
       ^
    <--l,r -->

    maxSubLent = 0
    for i in range(len(s)):
        #Odd maxSubLen
        maxSubLent = helper(s,maxSubLent,i,i)

        # Even maxSubLen
        maxSubLen = helper(s,maxSubLent,i,i+1)

    return maxSubLent

    def helper(s, l, r):
        while l > 0 and r < len(s) and s[l] == s[r]:
            if r-l+1 > maxSubLent:
                maxSubLent = r-l+1
            l -= 1
            r += 1
        return maxSubLent
  
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        resLen = 0
        res = ""

        for i in range(len(s)):
            # Odd maxSubLent
            l,r=i,i
            while l >=0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > resLen:
                    resLen = r-l+1
                    res = s[l:r+1]
                l -= 1
                r += 1
            # Even
            l,r = i, i+1
            while l >=0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > resLen:
                    resLen = r-l+1
                    res = s[l:r+1]
                l -= 1
                r += 1

        return res


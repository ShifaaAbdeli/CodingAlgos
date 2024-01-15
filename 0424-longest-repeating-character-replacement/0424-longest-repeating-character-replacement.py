class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # - use the sliding window with two pointers l and r
        # - use HashMap for each charactere count in string s
        # -  window size is r-l+1. We reduce left of the window when size > k
        charCount = {}
        res = 0
        l = 0
        maxf = 0
        
        for r in range(len(s)):
            charCount[s[r]] = 1 + charCount.get(s[r], 0)
            maxf = max(maxf, charCount[s[r]]) #This is an optimization, hard to see
            #while (r - l + 1) - max(charCount.values()) > k:
            while (r - l + 1) - maxf > k:
                charCount[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res
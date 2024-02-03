"""
s = "abc"
- Use of two pointers approach l and r:

1 - Use it for the case: a  b  c
                         ^^
                         lr
  - l and r start at same poistion i
  - then move l left and r ight
  
2 - Use it for the case: a b c
                         ^ ^
                         l r
  - l and r start at poistion l = i and r = i + 1
  - then move l left and r right
  
"""
class Solution:
    def countSubstrings(self, s: str) -> int:
        numberPalindrom = 0
        L = len(s)
        if L == 0:
            return numberPalindrom
        
        for i in range(L):
            l = r = i
            while l >= 0 and r < L and s[l] == s[r]:
                numberPalindrom += 1
                l -= 1
                r += 1
            # Case of l = i and r = i+1
            l = i
            r = i+1
            while l >= 0 and r < L and s[l] == s[r]:
                numberPalindrom += 1
                l -= 1
                r += 1
        return numberPalindrom

    ## Time complexity: O(n^2). Space: O(1)
        
        
        
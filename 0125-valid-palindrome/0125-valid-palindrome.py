class Solution:
    def isPalindrome(self, s: str) -> bool:
        # First Approach:
        # B.Force:
        #s = ''.join(c for c in s if c.isalnum())
        #s = s.lower()
        #return s == s[::-1]

        
        # Second approach:
        # Removing non-alphanumeric characters. 
        # and compare the charactaires
        l, r = 0, len(s) - 1

        # Alpha Numiric function:
        def alphaNum(c):
            return (ord('a') <= ord(c) <= ord('z') or
                    ord('A') <= ord(c) <= ord("Z") or
                    ord('0') <= ord(c) <= ord('9'))
                
        while l < r:
            while l < r and not alphaNum(s[l]):
                l += 1
            while l < r and not alphaNum(s[r]):
                r -= 1
                
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
            
        return True
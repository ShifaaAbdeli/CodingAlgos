class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = ''.join(c for c in s if c.isalnum())
        s = s.lower()
        return s == s[::-1]
        # Removing non-alphanumeric characters
        #s = ''.join(filter(str.isalnum, s))
        # Convert the string to lower cases
        #s = s.lower()
        # Use two pointers approch Left and Right
        #for i in range(len(s) - 1):
        #    if s[i] != s[len(s) - 1 -i]:
        #        return False
        #return True
        #return s == s[::-1]

        
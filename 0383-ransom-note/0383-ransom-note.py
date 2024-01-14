class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        # Does build a hashMap with the count 
        # of each carachtaire in the magazine str.
        # key,value (char, its count)
        letters = collections.Counter(magazine)
        
        # Check if the char count can form rge ransomNote
        for c in ransomNote:
            if letters[c] <= 0:
                return False
            letters[c] -= 1
        return True
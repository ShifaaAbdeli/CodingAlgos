class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        dict_p_s = {}
        dict_s_p = {}
        patternList = list(pattern)
        sList = list(s.split(" "))
        
        if len(patternList) != len(sList):
            return False

        for char1, char2 in zip(patternList, sList):
            if char1 not in dict_p_s and char2 not in dict_s_p:
                dict_p_s[char1] = char2
                dict_s_p[char2] = char1
            elif dict_p_s.get(char1) != char2 or dict_s_p.get(char2) != char1:
                return False
        return True
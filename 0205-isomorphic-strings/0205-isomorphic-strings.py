class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        #if len(s) != len(t):
        #    return False

        #sLetters = collections.Counter(s)
        #tLetters = collections.Counter(t)
        #sValues = list(sLetters.values())
        #tValues = list(tLetters.values())
        #if sValues != tValues:
        #        return False
        #return True
        dict_s_t = {}
        dict_t_s = {

        }
        for char1, char2 in zip(s,t):
            if (char1 not in dict_s_t) and (char2 not in dict_t_s):
                dict_s_t[char1] = char2
                dict_t_s[char2] = char1
            elif dict_s_t.get(char1) != char2 or dict_t_s.get(char2) != char1:
                return False
        return True


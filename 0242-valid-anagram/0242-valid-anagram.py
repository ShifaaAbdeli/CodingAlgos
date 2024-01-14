class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        dict_s, dict_t = {}, {}

        for c in s:
            dict_s[c] = dict_s.get(c, 0) + 1
        for cc in t:
            dict_t[cc] = dict_t.get(cc, 0) + 1

        return dict_s == dict_t


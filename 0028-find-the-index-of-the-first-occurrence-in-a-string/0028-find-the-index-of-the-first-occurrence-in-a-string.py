class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        res = [-1] * len(haystack)
        i = 0
        j = 0
        n = len(haystack)
        m = len(needle)
        for i in range(n):
            if len(haystack[i:m+i]) != m:
                break
            if needle == haystack[i:m+i]:
                res[j] = i
                j += 1
        return res[0]    
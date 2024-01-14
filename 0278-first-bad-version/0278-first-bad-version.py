# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 1
        r = n
        minVers = n
        while l <= r:
            mid = l + (r-l)//2
            badVers = isBadVersion(mid)

            if badVers == True:
                r = mid - 1
                minVers = min(minVers, mid)
            else:
                l = mid + 1
        return minVers



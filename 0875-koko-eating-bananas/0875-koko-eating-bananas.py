class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        ### Binary search approach. 
        # Use the piles as the array for left, mid and right.
        # k as min of of the calulated midKRate and 
        # the prevoise k
        # math.ceil() is new I had to look it up.
        l = 1
        r = max(piles)
        k = r

        while l <= r:
            midKRate = l + (r-l)//2
            totalHours = 0

            for pile in piles:
                totalHours += math.ceil(pile/midKRate)
            
            if totalHours <= h:
                k = min(k, midKRate)
                r = midKRate - 1
            else: 
                l = midKRate + 1
        return k

    ### Time complexity O(log(n)). Space O(1)



class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # - Use tree approach: example: Numbers chosen from range [1, n]
        # - Example: n = 4 and k = 2  
        # - 1 ---> 2, 3, 4 and 5
        # - 2 ---> 3, 4 and 5
        # - 3 ---> 4 and 5
        # - 4 ---> 5
        # - 5 nothing
        combArr = []
        curComb = []

        def combHelper(i):

            if len(curComb) == k:
                combArr.append(curComb.copy())
                return
            if i > n:
                return

            # Include comb i
            curComb.append(i)
            combHelper(i+1)

            # Not to include comb i
            curComb.pop()
            combHelper(i+1)

        combHelper(1)
        return combArr

        ## Time complexity: O(k*2^n). Space: O(n)
            
        
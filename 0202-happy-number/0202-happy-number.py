class Solution:
    def isHappy(self, n: int) -> bool:
        # Compute the sum from n as input of 
        # each diget's sqr of each n%10
        def sqrSum(n):
            total_sqrSum = 0
            while n > 0:
                # divmod provide the divident and diget of n%10
                n,mod = divmod(n, 10)
                total_sqrSum += mod ** 2
            return total_sqrSum

        setIsHappy = set()
        while n != 1 and n not in setIsHappy:
            setIsHappy.add(n)
            n = sqrSum(n)

        return n == 1
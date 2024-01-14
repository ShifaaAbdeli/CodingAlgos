class Solution:
    cashDict = {0:0, 1:1}

    def fib(self, n: int) -> int:
        ### Recursice approch

        #if n <= 1:
        #    return n
        #return (self.fib(n-2) + self.fib(n-1))

        ## For this approach, Time complexity O(2^n) and 
        ## Space complexity O(n) because the recursivity 
        ## and fucntion call use stack


        ### Using the Memoization approach

        # ---> See the cashDic defined above
        #if n in self.cashDict:
        #    return self.cashDict[n]
        #self.cashDict[n] = self.fib(n-1) + self.fib(n-2)
        #return self.cashDict[n]
        ## This approach the Time complexity is O(n) and 
        ## the space cpmlexity is O(n)


        #### Iterative bottom-up approach
        if n <= 1:
            return n
        curr = 0
        prev1 = 1
        prev2 = 0
        for i in range(2,n+1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr
        return curr
        ## Time complexity is O(n) and 
        ## Space Complexity is O(1)

        
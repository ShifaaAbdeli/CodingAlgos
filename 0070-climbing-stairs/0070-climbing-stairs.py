class Solution:
    def climbStairs(self, n: int) -> int:

        #one, two = 1, 1
        #for i in range(n -1):
        #    temp = one
        #    one = one + two
        #    two = temp
        #return one


        #### DP approach ####
        #### f(n) = f(n-1) + f(n-2) ####
        ### Examples: f(3) = f(2) + f(1) = 3 ###
        ### f(4) = f(3) + f(2) = 3 + 2 = 5 ###
        m_1, m_2 = 1, 1
        for i in range(n-1):
            temp = m_1
            m_1 = m_1 + m_2
            m_2 = temp
        return m_1

        ### Time complexity O(n) and Space O(1)

        
"""
n = 2 --- [0, 1, 2]  ===> ans= [0]
n = 5 --- [0, 1, 2, 3, 4, 5]  ===> ans= [0]
i = 1, 1 != offset * 2 --- offset = 2, ans[1] = ans[i=1 - offset=1] + 1 = 1
i = 2, if 2 == offset * 2 --- offset = 2, ans[2] = ans[i=2 - offset=2] + 1
i = 3, 3 != 2*2 --- offset = 2 --- ans[3] = ans[3 - offset=2] + 1 = 2, ans[0, 1, 2]

"""


class Solution:
    def countBits(self, n: int) -> List[int]:
        offset = 1
        ans = [0]*(n+1)
        for i in range(1,n+1):
            if offset * 2 == i:
                offset = i
            ans[i] = ans[i - offset] + 1
            
        return ans
            
            
            
        
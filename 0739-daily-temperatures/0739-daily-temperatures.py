"""
   temperatures = [73,74,75,71,69,72,76,73], 
1- B.F approche:
        - Use two loop to find a higher temperature then ith day.
        - This can get the time complexity O(n^2)
2- Second approach:
        - Use data structure stack where to cash 
           index i and its temperatures[i].
        - traverse the tepmperatures array and use the 
            stack index, temperature to compute the number of days.
        -Time complexity: O(n), space: O(n)
        
"""

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0]*n
        stack = []
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackTemp, stackIndx = stack.pop()
                res[stackIndx] = i - stackIndx
            stack.append([t, i])
            
        return res
        
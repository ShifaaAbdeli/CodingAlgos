class Solution(object):
    def sortedSquares(self, arr):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(arr)
        R = n-1
        L = 0
        highIndex = n-1
        squares = [0 for x in range(n)]
        
        if len(arr) == 0:
            return squares
  
        while R >= L:
            rightSquare = arr[R] * arr[R]
            leftSquare = arr[L] * arr[L]
            if rightSquare < leftSquare:
                squares[highIndex] = leftSquare
                L += 1
            else:
                squares[highIndex] = rightSquare
                R -= 1

            highIndex -= 1
            
        return squares  
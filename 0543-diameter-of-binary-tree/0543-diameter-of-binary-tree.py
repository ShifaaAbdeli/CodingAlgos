"""
1- Need to get the Hight and Diametter of the binary tree
2- Need to use DFS Algo to compute the Hight and also Diametter
3- Need to use recursive Datastructure
4- Time complexity: O(n), Space: O(n)

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = [0]
        
        def dfs(root):
                if root is None:
                    return -1
            
                left = dfs(root.left)
                right = dfs(root.right)
                diameter[0] = max(diameter[0], 2 + left + right) #Computing B.T diammeter
                return (1 + max(left, right)) # returning hight
        
        dfs(root)
        return diameter[0]
             
            
        
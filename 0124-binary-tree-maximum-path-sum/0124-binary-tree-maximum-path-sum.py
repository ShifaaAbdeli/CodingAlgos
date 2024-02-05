"""
- DFS approach:
   - Calculate max path of left
   - Calculate max path of right
   - Compute the max path of a of subthree
   - Return the max path of subtree to the immidiate root node parent
   
   - Time complexity is O(n). Space O(1)
   
"""



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]
        
        def dfs(root):
            
            if not root:
                return 0
            
            maxLeft = dfs(root.left)
            maxLeft = max(maxLeft, 0)
            maxRight = dfs(root.right)
            maxRight = max(maxRight, 0)
            
            #Compute the max path for a subtree woth split (left, right)
            res[0] = max(res[0], root.val + maxLeft + maxRight)

            # Compute and return the max path of 
            # each side (left or right) to root of a subtree
            return (root.val + max(maxLeft, maxRight))
        
        # Call the dfs with root node
        dfs(root)
        return res[0]
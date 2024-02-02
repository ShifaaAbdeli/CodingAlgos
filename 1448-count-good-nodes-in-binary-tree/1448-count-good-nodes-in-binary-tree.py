# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
                
        # Use DFS preorder approach:
        # Time cplexity: O(n). Space: O(n)
        
        def dfsHelper(node, maxVal):
            if not node:
                return 0
            res = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)
            
            res += dfsHelper(node.left, maxVal)
            res += dfsHelper(node.right, maxVal)
            return res
        
        return dfsHelper(root, root.val)
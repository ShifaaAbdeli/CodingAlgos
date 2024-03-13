"""
 Input: root = [4,2,7,1,3,6,9]
 tmp = 2
 left = 7
 right = tmp = 2
 4, 7, 2, 1,3,6,9
 
 tmp = 7.6
 left = 9
 right = tmp = 6
 4,7,2,9,6,1,3
 
 tmp = left = 2.1
 left = 3
 right = tmp = 1
 4,7,2,9,6,3,1
 
 - tmp = r.left
   r.left = r.right
   r.right = tmp
   invertTree(r.left)
   invertTree(r.right)
   
  Time Complexity: O(n), Space: O(1)
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root or root == []:
            return root
        
        head = root
        tmp = root.left
        root.left = root.right
        root.right = tmp
        
        if root.left:
            self.invertTree(root.left)
        if root.right:
            self.invertTree(root.right)
            
        return head
        
        
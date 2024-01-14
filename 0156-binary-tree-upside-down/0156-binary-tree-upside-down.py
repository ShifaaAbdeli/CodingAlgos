# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    # Write your code here.
    
        if root is None or root.left is None:
            return root
    
        oldLeft = root.left
    
        newRoot = self.upsideDownBinaryTree(root.left)
        oldLeft.left = root.right
        oldLeft.right = root
        root.left = None
        root.right = None

        return newRoot
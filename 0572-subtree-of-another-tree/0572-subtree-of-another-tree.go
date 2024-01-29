# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        def sameTree(self, s, t):
            if not s and not t:
                return True
            if s and t and s.val == t.val:
                return (sameTree(self, s.left, t.left) and
                       sameTree(self, s.right, t.right))
            return False
        
        if sameTree(self, root, subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or
            self.isSubtree(root.right, subRoot))
        

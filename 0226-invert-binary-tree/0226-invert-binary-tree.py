# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root

        deq = deque([root])
        while deq:
            p = deq.pop()
            p.left,p.right = p.right,p.left
            if p.left:
                deq.append(p.left)
            if p.right:    
                deq.append(p.right)
        return root

        # Recursive approch
        # if root is None:
        #   return root
        # p.left, p.right = p.right, p.left
        # if p.left is not None:
        #   invesTree(p.left)
        # if p.right is not None:
        #    inversTree(p.right)
        # return root
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        deq = deque([root])
        deq.append(root)
        while deq:
            p, q = deq.pop(), deq.pop()
            if p is None and q is None:
                continue
            if p is None or q is None:
                return False
            if p.val != q.val:
                return False
            deq.append(p.left)
            deq.append(q.right)
            deq.append(p.right)
            deq.append(q.left)
        return True
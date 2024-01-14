# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def checkTwoNodes(p, q):
            if p is None and q is None:
                return True
            if p is None or q is None:
                return False
            if p.val != q.val:
                return False
            return True

        queue = deque([(p,q)])
        while queue:
            p, q = queue.pop()
            if checkTwoNodes(p, q) == False:
                return False
            if p:
                queue.append((p.left, q.left))
                queue.append((p.right, q.right))
        return True
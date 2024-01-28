# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        """ BFS Approach
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
        """
        # DFS Recursive approch
        if root is None:
           return root
        root.left, root.right = root.right, root.left
        if root.left is not None:
            self.invertTree(root.left)
        if root.right is not None:
            self.invertTree(root.right)
        return root
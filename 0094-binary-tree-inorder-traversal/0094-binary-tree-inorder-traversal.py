# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        List = []
        """
        def helper(root):
            if not root:
                return
            helper(root.left)
            List.append(root.val)
            helper(root.right)
        
        helper(root)
        return List
        """
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            
            if not stack:
                return List
            
            node = stack.pop()
            List.append(node.val)
            root = node.right
            
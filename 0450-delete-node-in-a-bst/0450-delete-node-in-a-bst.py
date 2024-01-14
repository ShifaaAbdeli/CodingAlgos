# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minNode(self, curr: Optional[TreeNode]):
        while curr and curr.left:
            curr = curr.left
        return curr

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return root
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else: # key = root.val
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            else: # root.left nd root.right are not None.
                # Find the min node of the right sub tree of
                # the current root (not initial root !!)
                minTreeNode = self.minNode(root.right)
                # Update the currrent removal root with 
                # the minTreeNode val.
                root.val = minTreeNode.val
                # remove the minTreeNode
                root.right = self.deleteNode(root.right, minTreeNode.val)
        return root



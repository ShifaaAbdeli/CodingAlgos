# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    #    if root is None:
    #        return False

    #    targetSum -= root.val
        #leaf level
    #    if root.left is None and root.right is None:
    #        return targetSum == 0
        
    #    return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)

        # Time complexity O(n) and Space worst complexity is O(n) if all has a left shild (linear)

        if root is None:
            return False
        targetSum -= root.val
        if root.left is None and root.right is None:
            if targetSum == 0:
                return True
            else:
                targetSum += root.val
                return False
        if self.hasPathSum(root.left, targetSum):
            return True
        elif self.hasPathSum(root.right, targetSum):
            return True
        return False
        
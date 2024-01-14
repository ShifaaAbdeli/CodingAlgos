# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helperToBST(left, right):
            if left > right:
                return None
            # In PreOrder the Left middle is the root node for the BST
            pivot = (left + right) // 2

            # Preorder traversal: Root --> Left --> Right
            root = TreeNode(nums[pivot])
            root.left = helperToBST(left, pivot-1)
            root.right = helperToBST(pivot+1, right)
            return root

        return helperToBST(0, len(nums) - 1)

# In This preorder, Time Complexity is O(N) and 
# Space complexity is O(logN)
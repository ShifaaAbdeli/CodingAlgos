# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        nodesVal = []
        # We se inorder traversal because 
        # handle the nodes in sorted order.
        def dfsInOrder(node):
            if node is None:
                return
            dfsInOrder(node.left)
            nodesVal.append(node.val)
            dfsInOrder(node.right)

        dfsInOrder(root)
        nodesVal.sort()
        minDiff = 1e9 # Initialize to infinity
        for i in range(1, len(nodesVal)): # start from 1 for the diff
            minDiff = min(minDiff, nodesVal[i] - nodesVal[i-1])

        return minDiff

        # Time Complexity is O(n) and space is O(n)


            
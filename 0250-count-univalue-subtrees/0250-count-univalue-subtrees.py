# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        """
        Args:
         root(BinaryTreeNode_int32)
        Returns:
         int32
        """
        # Write your code here.

        # Thinking of using the botom up DFS approch, since the 
        # subtrees counting seems to be easy to start from the bottom.
        # Information needed to get from each node are:
        # 1- Is node unival ? 
        # 2- How many subtree count under the node ?

        if root is None:
            return 0

        # unival_dfs ( ) shall return isUnival and subtreeCount
        def unival_dfs(node):

            #nonlocal subTreeUnivalCount
            isUnival = True
            subTreeUnivalCount = 0

            # Base case for leaf worker
            if node.left is None and node.right is None:
                return (1,True)

            # Recursive base for left and right of a node
            if node.left is not None:
                (leftSubTreeUnivalCount, isLeftUnival) = unival_dfs(node.left)
                if isLeftUnival == False or node.left.val != node.val:
                    isUnival = False

                subTreeUnivalCount = subTreeUnivalCount + leftSubTreeUnivalCount

            if node.right is not None:
                (rightSubTreeUnivalCount, isRightUnival) = unival_dfs(node.right)
                if isRightUnival == False or node.right.val != node.val:
                    isUnival = False

                subTreeUnivalCount = subTreeUnivalCount + rightSubTreeUnivalCount

            if isUnival:
                subTreeUnivalCount = subTreeUnivalCount + 1

            return (subTreeUnivalCount, isUnival)


        (subTreeUnivalCount, isUnival) = unival_dfs(root)
        return subTreeUnivalCount    
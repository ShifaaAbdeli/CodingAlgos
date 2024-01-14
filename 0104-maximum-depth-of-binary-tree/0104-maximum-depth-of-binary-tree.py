# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0

        stack = []
        stack.append((1,root))

        depth = 0
        while stack != []:
            depth_count, node = stack.pop()

            if node is not None:
                depth = max(depth, depth_count)
                stack.append((depth_count + 1, node.left))
                stack.append((depth_count + 1, node.right))

        return depth

        node = root
        depth_left, depth_right = 0,0
        while node is not None:
            if node.left is not None:
                depth_left += 1
                node = node.left
            elif node.right is not None:
                depth_right += 1
                node = node.right
        return max(depth_left, depth_right)+1
        
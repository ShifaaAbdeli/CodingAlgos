# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', a: 'TreeNode', b: 'TreeNode') -> 'TreeNode':
        
        # Write your code here.

        #if root.left is None and root.right in None:
        #    return root.value
        if not root:
            return
        elif a.val == root.val or b.val == root.val:
            return root
        else:
            leftN = self.lowestCommonAncestor(root.left, a, b)
            #print ("DFS leftN", leftN.val)
            
            rightN = self.lowestCommonAncestor(root.right, a, b)
            #print ("DFS rightN", rightN.val)

            if ((leftN == a and rightN == b) or
                (leftN == b and rightN == a)):
                #print("root.val", root.val)
                return root

            if leftN is None and rightN:
                #print("leftN is 0, rightN ", rightN.val)
                return rightN

            if leftN and rightN is None:
                #print("rightN is 0 and leftN ", leftN.val)
                return leftN
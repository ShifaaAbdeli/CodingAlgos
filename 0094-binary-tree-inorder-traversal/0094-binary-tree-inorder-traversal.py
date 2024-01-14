# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    ### Recursive ####

        #out = []
        #def helper(root):
        #    if not root:
        #        return root
        #    helper(root.left)
        #    out.append(root.val)
        #    helper(root.right)

        #helper(root)
        #return out
    ### Time complexity O(log(n)). Space O(n)

    ###### Iterative approach ####
    # 1- Create a stack and append all left child on it.
    # 2- Pop the top of the stack. And append it to an array.
    # 3- Append the right child of the top node.
    # 4- return the array
        out = []
        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            out.append(curr.val)
            curr = curr.right
        return out


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ### Recursive approach ###
        #out = []
        #def helperInOrder(curr):
            #if not curr:
                #return curr

            #helperInOrder(curr.left)
            #out.append(curr.val)
            #helperInOrder(curr.right)

        #helperInOrder(root)
        #return out[k-1]

    ## Time complexity is O(log(n)). Space O(n)

    ####### Iterative approach  ######
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop() # this is the k+1 smallest element 
                               # pop from the stack
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right


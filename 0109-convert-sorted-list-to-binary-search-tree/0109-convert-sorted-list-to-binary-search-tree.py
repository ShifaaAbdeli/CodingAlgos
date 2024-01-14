# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        curr = head
        arr = []

        while curr is not None:
            arr.append(curr.val)
            curr = curr.next

        def helper(arr, start, end):

            #Base Case
            if start > end:
                return None
            elif start == end:
                return TreeNode(arr[start])

            # Recursive case
            mid = start + (end - start)//2
            root = TreeNode(arr[mid])

            # left start ... mid-1
            # right mid+1 ... end
            root.left = helper(arr, start, mid-1)
            root.right = helper(arr, mid+1, end)

            return root
        
        return (helper(arr, 0, len(arr)-1))
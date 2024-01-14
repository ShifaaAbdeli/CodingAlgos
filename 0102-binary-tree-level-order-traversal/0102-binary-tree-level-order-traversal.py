#from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        lists = []
        if not root:
            return root

        queue = deque()
        queue.append(root)
        while len(queue):
            arr = []
            for i in range(len(queue)):
                curr = queue.popleft()
                arr.append(curr.val)
                if (curr.left):
                    queue.append(curr.left)
                if (curr.right):
                    queue.append(curr.right)

            lists.append(arr)

        return lists
### Time complexity is O(n), Space O(n)
              

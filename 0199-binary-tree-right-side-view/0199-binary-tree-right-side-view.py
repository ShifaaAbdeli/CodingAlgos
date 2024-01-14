# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        queue = deque()
        queue.append(root)

        while queue:
            qLen = len(queue)
            rightSide = None
            for i in range(qLen):
                Node = queue.popleft()
                if Node:
                    rightSide = Node
                    queue.append(Node.left)
                    queue.append(Node.right)
            if rightSide:
                arr.append(rightSide.val)
        return arr

    ### Time complexity is O(n)), Space O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        que = deque([root])
        avreg = []
        while que:
            # qsize represent the number of node per level.
            # When it is null mean we travese entive level.
            qsize = len(que)
            count = 0
            sumNodes = 0
            for _ in range (qsize):
                node = que.popleft()

                if node:
                    sumNodes += node.val
                    count += 1

                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            avreg.append(sumNodes/count)

        return avreg
        



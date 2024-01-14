# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#def zigzag_level_order_traversal(root):
import collections 

class Solution:
     def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
            
            # base case
            if root is None:
                return []
    
            result = []
            q = collections.deque([root])
            level = 1
    
            while len(q) != 0:
                temp = []
                numNodes = len(q)
        
                for _ in range(numNodes):
                    node = q.popleft()
                    if node.left is not None:
                        q.append(node.left)
                    if node.right is not None:
                        q.append(node.right)
                    temp.append(node.val)

                #if level == 1:
                    #result.append(temp)
                if level == 0:
                    temp.reverse()
                    
                result.append(temp)
                level = not level
        
            return result
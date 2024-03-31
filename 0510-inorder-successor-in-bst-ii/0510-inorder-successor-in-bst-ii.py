"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':
        if node.right:
            cur = node.right
            while cur.left:
                cur = cur.left
            return cur
        else:
            cur = node.parent
            while cur and cur.val < node.val:
                cur = cur.parent
            return cur
        
        return None
                
## Time complexity: O(log(n)), Space: O(1)            
            
        
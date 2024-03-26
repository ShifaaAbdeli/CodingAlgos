"""
Input: root = [5,3,6,2,4,null,7], key = 3

- Search on the BST for the node.val = 3
- Check if the node.val = 3 has one child or two childs
  - If it has one chiled, delete and connect the child node with the grand parent
  - If it has two childs, seach for the min child (val = 2) and swap it with the node.val (= 3).

Time Complexity: O(log(n)), Space : O(1) 


"""



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                # find min node from right subtree:
                cur = root.right
                while cur and cur.left:
                    cur = cur.left
                root.val = cur.val
                root.right = self.deleteNode(root.right, cur.val)
        
        return root        
        
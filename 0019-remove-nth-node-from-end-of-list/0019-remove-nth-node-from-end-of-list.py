# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # USE TWO POINTERS APPROACH
        
        # use a dummy ptr: dummy --> head --> 1 --> 2 --> 3 --> 4 
        dummy = ListNode(0, head)
        
        left, right = dummy, head
        
        # Move right ptr to get to offset+1 from the
        # left since left is initialy pointing to dummy:
        # ptr: left <-- n+1 --> right.
        while n > 0 and right:
            right = right.next
            n -= 1
            
        # When right ptr is at null ptr, left is at Nth-1 element    
        while right:
            left = left.next
            right = right.next
        
        # Delete the Nth element
        left.next = left.next.next
        
        return dummy.next
        
## Time complexity: O(n), Space:O(1)
            
            
            
        
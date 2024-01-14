# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        # Use the two pointer approash, 
        # Slow move by one element and 
        # fast move by two elements
        slow = head
        fast = head.next
        while slow != fast:
            # fast or fast.next reach null 
            # then no cycle in this linked list
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
        # Time complexity is O(n) we travese each node once
        # Space complexity is O(1), no additional memory or storage.
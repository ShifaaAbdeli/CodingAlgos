"""
5--> 4 --> 2 --> 1
slow: a step at the time
fast: two step at the time

when fast.next = null, then slow is at the 
half position in liked List.

5--> 4 --> 2 --> 1
SF   
     s     f
slow, fast = head, head
prev = None
while fast and fast.next:
    fast = fast.next.next
    temp = slow.next
    slow.next = prev
    prev = slow
    slow = temp
    # null <--- 5 <--- 4 <--- 2 ---> 1
    #.               prev    slow        fast

    res = 0
    while slow:
        res = max(res, prev.val + slow.val)
        prev = prev.next
        slow = slow.next
    return res

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # 5--> 4 --> 2 --> 1
        # sf 
        slow, fast = head, head
        prev = None

        while fast and fast.next:
            fast = fast.next.next
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
            # null <--- 5 <--- 4 <--- 2 ---> 1
            #.                prev   slow        fast

        res = 0
        while slow:
            res = max(res, prev.val + slow.val)
            prev = prev.next
            slow = slow.next
        return res

        ## Time: O(n). Space: O(1)
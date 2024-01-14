# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        1- we can use B.F approach, by deviding the lenght of liked list by two
        2- we use the two pointers slow anf fast approach. 
           - The fast pointer is two time faster than slow pointer s.
           - When the faster pouinter f reach the end of linked list s in at midle.
           - we retirn slow pointer s
        """
        s,f = head, head

        while f and f.next:
            s = s.next
            f = f.next.next
        return s
    ## Time complexity: O(n), Space : O(1)

        
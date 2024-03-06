"""
[
  1->4->5,
  1->3->4,
  2->6
]
- B.F: 
  Merge linked list by linked list. The Time complexity O(k*n)

To avoid to repete the merging each linked list and improve the 
time complexity we can merge two linkedList by two linkedList: 
   example:
    - merge 1->4->5 and 1->3->4 ===> 1->1->3->4->4->5
    - merge 1->1->3->4->4->5 and 2->6

Approach:
- Merge each two linked list i and i+1 and 
  append them in new mergerList (list of merged linked lists).
- return the head of final merged list
- build the merge function of two linked list
- Time comlexity is n*log(k), since we keep dividing the lists by 2 logk times
  Space complexity is: O(k)

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists is None or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergeList = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                mergeList.append(self.mergeTwoList(l1, l2))
            lists = mergeList

        return lists[0]

    def mergeTwoList(self, l1, l2):
        dummy = ListNode()
        tail = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            # tail.next already filled, move to the tail.next
            tail = tail.next

        if l1:
            tail.next = l1
        if l2:
            tail.next = l2

        return dummy.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        
        - Approach 1: Use of two pointers approach
               - Define a third link list3
               - Find the middle of the link List using two pointers
                 approach Slow and Fast
               - Reverse the second hallf of the link list
               - Interleave the insertion of nodes in the Link list3 from 
                 the first half and second half of the link List
               Time complexity:O(n). Space coplexity: O(n)
                 
        - Approach 2: Improved the space complexity
                - Do the approach 1 inplace (without link List3 )
                Time complexity: O(n). Space complexity: O(1)
        """
        # find the midle of the link list
        slow, fast = head, head.next
        while fast and fast.next: # not reaching the end
            slow = slow.next
            fast = fast.next.next
            
        # slow is at the midle now and slow.next at the begining 
        # of the second half.
        # Reverse the second half
        #1 --> 2 --> 3 --> 4 --> 5 --> 6  
        #            ^     ^    temp
        #           slow  second 
                          

        second = slow.next
        prev = slow.next = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
            
        # Alternate the link list's fist half and the reversed second half
        #        1 --> 2 --> 3   4 <-- 5 <-- 6  
        #        ^                           ^ 
        #    head.next                      prev
                          
        l1, l2 = head, prev
        while l1 and l2:
            temp1 = l1.next
            temp2 = l2.next
            l1.next = l2
            l2.next = temp1
            l1, l2 = temp1, temp2

            
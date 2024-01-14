# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ### Intuitive idea is to use mergeSort algo in
        ### this list of link_Lists.

        # 1- merge two linkedList, from Lists, at the time.
        # and the result of this two linkedlist merge to be
        # stored in one of the two list.
        amountOfList = len(lists)
        numOfList = 1

        # In each while itiration we mergeSort each 
        # two linkedlists... until we merge them 
        # all in list[0]
        while numOfList < amountOfList:
            for i in range(0, amountOfList - numOfList, numOfList * 2):
                lists[i] = self.mergeSortTwoList(lists[i], lists[i + numOfList])
            numOfList *= 2

        return lists[0] if amountOfList > 0 else None

    ### MergeSortTwoList sort for two sorted link list.
    def mergeSortTwoList(self, l1, l2):
        head = node = ListNode(0)

        while l1 and l2:
            if l1.val <= l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                ## This two steps below are hard steps to 
                ## think about them during interview.
                # So, since we are merging to two list 
                # into list[i], then we need to point l2 
                # to the remaining of l1 linked list. And then
                # point l1 to the node.next.next where 
                # we stind now  
                l2 = l1
                l1 = node.next.next
            node = node.next

        if not l1:
            node.next = l2
        else:
            node.next = l1
        
        return head.next
            

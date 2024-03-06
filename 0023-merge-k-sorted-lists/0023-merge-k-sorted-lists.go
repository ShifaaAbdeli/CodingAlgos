/*
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

*/

func mergeTwoList(list1 *ListNode, list2 *ListNode) *ListNode {
    
    dummy := new(ListNode)
    tail := dummy
    
    for (list1 != nil && list2 != nil) {
        if list1.Val < list2.Val {
            tail.Next = list1
            list1 = list1.Next
        } else {
            tail.Next = list2
            list2 = list2.Next
        }
        tail = tail.Next
    }
    
    if list1 != nil {
        tail.Next = list1
    }
    if list2 != nil {
        tail.Next = list2
    }
    
    return dummy.Next
}

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func mergeKLists(lists []*ListNode) *ListNode {
    if lists == nil || len(lists) == 0 {
        return nil
    }
    
    for len(lists) > 1 {
        merge := []*ListNode{}
        
        for i:= 0; i < len(lists); i += 2 {
            if i+1 >= len(lists) {
                merge = append(merge, lists[i])
                continue
            }           
            merge = append(merge, mergeTwoList(lists[i], lists[i+1]))
        }
        lists = merge
    }
    return lists[0]
}
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func removeNthFromEnd(head *ListNode, n int) *ListNode {
    /*
       - Use two pointer approach:
         - Two ptrs left and right and maintine the offset between 
           of n between them.
         - 
       
    */
    dummy := &ListNode{Next: head}
    
    //The above left init to dummy to make sure
    //we stop at nth -1 element
    left, right := dummy, head 

    // Create the offset of n between left and right ptrs
    //for i := 0; i < n; i++ {
    for n > 0 && right != nil {
        right = right.Next
        n--
    }
    
    for right != nil {
        left = left.Next
        right = right.Next
    }
    left.Next = left.Next.Next
    
    return dummy.Next
    
}
// Time complexity O(n), space: O(1)
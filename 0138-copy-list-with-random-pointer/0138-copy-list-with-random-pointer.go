/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Next *Node
 *     Random *Node
 * }
 */

func copyRandomList(head *Node) *Node {
    copyToOld := make(map[*Node]*Node)
    
    cur := head
    for cur != nil {
        copy := &Node{Val: cur.Val}
        copyToOld[cur] = copy
        cur = cur.Next
    }
    cur = head
    for cur != nil {
        copy := copyToOld[cur]
        copy.Next = copyToOld[cur.Next]
        copy.Random = copyToOld[cur.Random]
        cur = cur.Next
    }
    
    return copyToOld[head]
}
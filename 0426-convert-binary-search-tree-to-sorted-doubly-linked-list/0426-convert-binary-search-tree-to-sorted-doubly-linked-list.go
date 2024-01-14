/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Left *Node
 *     Right *Node
 * }
 */

var head, tail *Node

func treeToDoublyList(root *Node) *Node {
    head = nil
    tail = nil
    
    if(root == nil) {
        return root
    }
    
    dfsTreeToDoublyList(root)
    head.Left = tail
    tail.Right = head
    
    return head
}

func dfsTreeToDoublyList(node *Node) {
    
    if(node == nil) {
        return
    }
    
    dfsTreeToDoublyList(node.Left)
    if(tail != nil) {
        tail.Right = node
        node.Left = tail
    }else {
        head = node
    }
    tail = node
    
    dfsTreeToDoublyList(node.Right)
}
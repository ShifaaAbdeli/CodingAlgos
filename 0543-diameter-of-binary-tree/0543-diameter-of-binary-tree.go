/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
import "math"

func diameterOfBinaryTree(root *TreeNode) int {
    var diameterOfBT float64;
    
    if (root == nil) {
        return 0;
    }
    dfsCountEdges(root, &diameterOfBT)
    return int (diameterOfBT);
}


func dfsCountEdges(n *TreeNode, diameterOfBT *float64) float64 {
    
    var left float64;
    var right float64;
    if(n == nil) {
        return 0
    }
    left = dfsCountEdges(n.Left, diameterOfBT)
    right = dfsCountEdges(n.Right, diameterOfBT)
    *diameterOfBT = math.Max(*diameterOfBT, left+right)
    return math.Max(left, right) + 1
    
}

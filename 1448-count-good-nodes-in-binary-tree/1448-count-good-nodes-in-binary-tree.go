/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func dfsHelper(node *TreeNode, maxVal int) int {
    res := 0
    if node == nil {
        return 0
    }
    if node.Val >= maxVal {
        res = 1
    } else {
        res = 0
    }
    maxVal = max(maxVal, node.Val)
    res += dfsHelper(node.Left, maxVal)
    res += dfsHelper(node.Right, maxVal)
    
    return res
}
func goodNodes(root *TreeNode) int {
    return dfsHelper(root, root.Val)
}

// Time Complexity: O(n). Space Complexity: O(1)
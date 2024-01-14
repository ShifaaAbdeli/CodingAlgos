/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isValidBST(root *TreeNode) bool {
    return (validateBST_DFS(root, nil, nil))
}

/*
 *  Use the DFS for this BST to validate 
 *  the left and right side of the tree as a BST
 */
func validateBST_DFS(node *TreeNode, LeftMin *TreeNode, RightMax *TreeNode) bool {
    
    if (node == nil) {
        return true
    }
    if (((LeftMin != nil) && (node.Val <= LeftMin.Val)) || ((RightMax != nil) && (node.Val >= RightMax.Val))) {
                return false
    }

    return (validateBST_DFS(node.Left, LeftMin, node) && validateBST_DFS(node.Right, node, RightMax))
    
}
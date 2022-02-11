'''
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
'''
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def helper(node, ma, mi):
            flag = node.val<ma and node.val>mi
            
            if node.left != None:
                flag = flag and helper(node.left, node.val, mi) 
            if node.right != None:
                flag = flag and helper(node.right, ma, node.val)   
                
            return flag
            
        ma, mi = float('inf'), float('-inf')
        return helper(root, ma, mi)
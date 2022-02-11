# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

 

# Example 1:


# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:        
        def helper(l, r):
            if l>r: return None            
            nonlocal p_index
            root = TreeNode(preorder[p_index])            
            mid = inorder.index(preorder[p_index])                       
            p_index+=1
            
            root.left = helper(l, mid-1)               
            root.right = helper(mid+1, r)
            return root
        
        p_index = 0
        return helper(0, len(inorder)-1)

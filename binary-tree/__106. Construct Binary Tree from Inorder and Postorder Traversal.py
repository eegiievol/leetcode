'''
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

 

Example 1:


Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: inorder = [-1], postorder = [-1]
Output: [-1]
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        def helper(l, r):
            nonlocal post_index
            if l>r:
                return None
            
            #find value of root node
            root_val = postorder[post_index]
            post_index -= 1

            #find index of root node
            mid = inorder.index(root_val)

            #build tree
            node = TreeNode(root_val)
            node.right = helper(mid+1, r)
            node.left = helper(l, mid-1)

            return node
        
        post_index = len(postorder)-1
        return helper(0, len(postorder)-1)
     

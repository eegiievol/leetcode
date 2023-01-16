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
            if l>r:
                return None
            cur = TreeNode(preorder[self.i])
            root_index = inorder.index(preorder[self.i])
            self.i += 1
            cur.left = helper(l, root_index-1)
            cur.right = helper(root_index+1, r)
            return cur
        
        self.i = 0
        return helper(0, len(preorder)-1)

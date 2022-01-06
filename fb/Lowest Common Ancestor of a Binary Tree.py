# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

# Example 1:


# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    ans = None
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'):
        def helper(node, a, b):
            if not node:
                return 0 
            itself = node==a or node==b 
            left = helper(node.left, a, b)
            right = helper(node.right, a, b)
            total=left+right+itself
            if total>=2:
                self.ans = node
            return left or right or itself        
        
        helper(root,p,q)
        return self.ans

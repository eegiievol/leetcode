'''
Given the root of a binary search tree and a node p in it, return the in-order successor of that node in the BST. If the given node has no in-order successor in the tree, return null.

The successor of a node p is the node with the smallest key greater than p.val.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    rightmost = None
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':         
        
        def helper(root, p, rm_parent):              
            if root == p:
                self.rightmost = rm_parent
                return
            if root.left!=None and p.val<root.val:                
                helper(root.left, p, root)
                return 
            if root.right!=None and p.val>root.val:
                helper(root.right, p, rm_parent)
                return
        
        if root==None:
            return None
        
        if p.right!=None:   #case1
            cur = p.right
            while cur.left:
                cur=cur.left
            return cur
        else: #case2
            helper(root, p, None)        
        return self.rightmost
        
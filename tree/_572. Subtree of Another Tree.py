# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

 

# Example 1:


# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.heads = []
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(r1, r2):
            if not r1 and not r2:
                return True       
            if not r1 or not r2:
                return False            
            return r1.val==r2.val and isSame(r1.left, r2.left) and isSame(r1.right, r2.right)
        
        def find(root, subroot):
            if not root:
                return
            if root.val==subroot.val:
                self.heads.append(root)                 
            find(root.left, subroot)
            find(root.right, subroot)
            
        find(root, subRoot)    
        if self.heads:
            for head in self.heads:
                if isSame(head, subRoot):
                    return True
        return False

#RECURSIVE
#============================================

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_same(root, sub):
            if root and sub:
                return root.val == sub.val and is_same(root.left, sub.left) \
                                    and is_same(root.right, sub.right)
            else:
                if root or sub:
                    return False
                else:
                    return True
        def find(root, sub):
            a = False
            if root:
                if root.val == sub.val:
                    a |= is_same(root, sub)
                a |= find(root.left, sub) 
                a |= find(root.right, sub)
            return a
    
        return find(root, subRoot)

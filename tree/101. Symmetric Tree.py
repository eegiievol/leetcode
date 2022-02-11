# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

# Example 1:


# Input: root = [1,2,2,3,4,4,3]
# Output: true

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def helper(left, right):
            if not left and not right:
                return True
            if (not left and right) or (left and not right):
                return False
            
            return left.val==right.val and helper(left.left, right.right) and helper(left.right, right.left)        
        return helper(root.left, root.right)
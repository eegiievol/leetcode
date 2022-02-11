# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

 

# Example 1:


# Input: root = [3,1,4,null,2], k = 1
# Output: 1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(root):
            nonlocal counter
            nonlocal ans
            if not root:
                return
            inorder(root.left)
            counter += 1
            if counter==k:
                ans = root.val
            inorder(root.right)
        
        counter = 0
        ans = float('-inf')
        inorder(root)
        return ans
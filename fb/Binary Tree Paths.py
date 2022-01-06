# Given the root of a binary tree, return all root-to-leaf paths in any order.

# A leaf is a node with no children.

 

# Example 1:


# Input: root = [1,2,3,null,5]
# Output: ["1->2->5","1->3"]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def helper(ans, node, path):
            if not node.right and not node.left:
                ans.append(path+str(node.val))
                return
            
            if node.right:
                helper(ans, node.right, path+str(node.val)+'->')                       
            if node.left:
                helper(ans, node.left, path+str(node.val)+'->') 
        
        ans=[]
        helper(ans, root, '')
        return ans

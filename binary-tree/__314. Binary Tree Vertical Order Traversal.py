'''
Given the root of a binary tree, return the vertical order traversal of its nodes' values. 
(i.e., from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Example 2:


Input: root = [3,9,8,4,0,1,7]
Output: [[4],[9],[3,0,1],[8],[7]]
Example 3:


Input: root = [3,9,8,4,0,1,7,null,null,null,2,5]
Output: [[4],[9,5],[3,0,1],[8,2],[7]]
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        def helper(level, node, row):
            if not node:
                return
            
            level_map[level].append((row, node.val))
            helper(level-1, node.left, row+1)
            helper(level+1, node.right, row+1)
        
        if not root:
            return []

        level_map = defaultdict(list)
        helper(0, root, 0)
    
        mi, ma = min(level_map.keys()), max(level_map.keys())

        ans = []
        for level in range(mi, ma+1):
            ans.append([x[1] for x in sorted(level_map[level], key=lambda x:x[0])])
        
        return ans

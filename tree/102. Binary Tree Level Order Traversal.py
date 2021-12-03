'''
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root == None:
            return None        
        lmap = {root:0}
        ans = []        
        q = deque()
        q.append(root)
        level=0
        while q:
            le = len(q)
            ans.append([])            
            for i in range(le):
                popped = q.popleft()                
                ans[level].append(popped.val)                
                if popped.left!=None:
                    q.append(popped.left)                    
                if popped.right!=None:
                    q.append(popped.right)   
            level+=1
            
            
        
        return ans
            
        
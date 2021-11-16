# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root):
        q = deque()
        ans=[]
        q.append(root)
        
        while q:
            popped=q.popleft()
            if not popped.left and popped.right:
                ans.append(popped.right.val)
                q.append(popped.right)
                continue
                
            if popped.left and not popped.right:
                ans.append(popped.left.val)
                q.append(popped.left)
                continue
            
            if popped.right and popped.left:
                q.append(popped.left)
                q.append(popped.right)
                
        return ans

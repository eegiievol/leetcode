# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[20,9],[15,7]]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        reverse = False
        q= deque()
        if root:
            q.append(root)
        while q:
            count = len(q)
            sub = []
            for _ in range(count):               
                popped = q.popleft()                 
                sub+=[popped.val]
                if popped.left:
                    q.append(popped.left)
                if popped.right:
                    q.append(popped.right)
            if reverse:
                ans.append(sub[::-1])
            else:
                ans.append(sub)
            reverse = not reverse
        return ans

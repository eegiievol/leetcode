# Definition for a binary tree node.
'''
Given the root of a binary tree, return the maximum width of the given tree.

The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), 
where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that 
level are also counted into the length calculation.

It is guaranteed that the answer will in the range of a 32-bit signed integer.

Example 1:
Input: root = [1,3,2,5,3,null,9]
Output: 4
Explanation: The maximum width exists in the third level with length 4 (5,3,null,9).

Example 2:
Input: root = [1,3,2,5,null,null,9,6,null,7]
Output: 7
Explanation: The maximum width exists in the fourth level with length 7 (6,null,null,null,null,null,7).

Example 3:
Input: root = [1,3,2,5]
Output: 2
Explanation: The maximum width exists in the second level with length 2 (3,2).
 
'''
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    #intuition: if node index is i, its left child index is i*2, right child index is i*2+1
    #once we know the index of nodes it will be a easy to find a distance using left, right pointers
        ans = 0
        if not root:
            return 0

        q = deque()
        q.append((root.leftåç, 2))
        q.append((root.right, 3))

        ans = 1
        while q:
            left = right = -1
            for i in range(len(q)):
                popped, index = q.popleft()
                if popped:
                    if left<0:
                        left = index
                    else:
                        right = index
                    if popped.left:
                        q.append((popped.left, index*2))
                    if popped.right:
                        q.append((popped.right, index*2+1))
            
            ans = max(ans, right-left+1)
        return ans

        

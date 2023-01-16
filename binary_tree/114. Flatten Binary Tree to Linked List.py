
'''
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.
'''

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def helper(cur): 
            #base case:1
            if cur.left == None and cur.right == None:
                return cur            
            #base case:2
            if cur.left == None:
                return helper(cur.right) 
            #base case:3
            if cur.right == None:              
                cur.right = cur.left
                cur.left = None
                return helper(cur.right)
            
            #main part
            tail = helper(cur.left)
            tail.right = cur.right
            cur.right = cur.left
            cur.left = None
        
            return helper(cur.right)
        
        if root == None:
            return 
        
        return helper(root)
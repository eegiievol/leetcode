# Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.

# You can think of the left and right pointers as synonymous to the predecessor and successor pointers in a doubly-linked list. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.

# We want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. You should return the pointer to the smallest element of the linked list.

 

# Example 1:



# Input: root = [4,2,5,1,3]


# Output: [1,2,3,4,5]

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:   
    def __init__(self):
        self.prev = None
        self.head = None
        
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':        
        def helper(root):
            if not root:                
                return 
                
            #INORDER TRAVERSAL
            helper(root.left)
            if not self.prev:
                self.head = root
            else:                
                root.left = self.prev
                self.prev.right = root
            self.prev = root  
            helper(root.right)
    
        if not root:
            return None

        helper(root)
        self.prev.right = self.head
        self.head.left = self.prev
        
        return self.head
        
        

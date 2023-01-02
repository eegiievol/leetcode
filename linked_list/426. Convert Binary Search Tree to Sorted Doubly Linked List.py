# Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.

# You can think of the left and right pointers as synonymous to the predecessor and successor pointers in a doubly-linked list. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.

# We want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. You should return the pointer to the smallest element of the linked list.

 

# Example 1:



# Input: root = [4,2,5,1,3]


# Output: [1,2,3,4,5]

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def helper(node):            
            if node:
                helper(node.left)
                if self.last:
                    #linking cur & last node
                    self.last.right = node
                    node.left = self.last
                else:
                    #case: leftmost branch
                    self.head = node        
                self.last = node
                helper(node.right)
        
        if not root:
            return None    
        
        self.first, self.last = None, None
        
        helper(root)
        self.last.right = self.head
        self.head.left = self.last
        return self.head
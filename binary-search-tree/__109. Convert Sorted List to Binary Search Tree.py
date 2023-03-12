'''
Given the head of a singly linked list where elements are sorted in ascending order, convert it to a 
height-balanced binary search tree.

Example 1:
Input: head = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.

Example 2:
Input: head = []
Output: []
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def build(l, r):
            if l>r:
                return None
            mid = (l+r) // 2
            left = build(l, mid-1)

            node = TreeNode(self.head.val)
            self.head = self.head.next
            
            node.left = left
            node.right = build(mid+1, r)
            return node
        
        def getLen(h):
            le = 0
            tmp = h
            while tmp:
                le += 1
                tmp = tmp.next
            return le
        
        self.head = head
        list_len = getLen(head)
        return build(0, list_len-1)
        

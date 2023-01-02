# Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

# Example 1:

# Input: head = [1,2,3,3,4,4,5]
# Output: [1,2,5]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode(0)
        sentinel.next = head
        
        prev = sentinel
        cur = head       
        while cur and cur.next:
            if cur.val == cur.next.val:
                while cur.next and cur.val == cur.next.val:
                    cur, cur.next = cur.next, cur.next.next
                prev.next = cur.next
                cur = cur.next
            else:
                prev, cur = cur, cur.next
        return sentinel.next


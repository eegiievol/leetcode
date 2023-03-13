'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        sentinel = ListNode(val=0, next=head)
        cur = sentinel

        for _ in range(n):
            cur = cur.next
            if not cur:
                return None

        l, r = sentinel, cur
        
        while r.next:
            l = l.next
            r = r.next
        
        l.next = l.next.next

        return sentinel.next
       

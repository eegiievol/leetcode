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
        sentinel = ListNode(0)
        sentinel.next = head
        left = right = sentinel
    
        #move right until distance(left,right)==n
        for _ in range(n):
            if right.next:
                right = right.next
            else:
                return []

        #move window
        while right.next:
            left = left.next
            right = right.next
            
        #remove
        left.next = left.next.next
        return sentinel.next
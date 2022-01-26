# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, p1: Optional[ListNode], p2: Optional[ListNode]) -> Optional[ListNode]:
        if not p1 and not p2:
            return None        
        if not p1:
            return p2
        elif not p2:
            return p1    
        
        if p1.val<p2.val:
            p1.next = self.mergeTwoLists(p1.next, p2)
            return p1
        else:
            p2.next = self.mergeTwoLists(p1, p2.next)
            return p2
        
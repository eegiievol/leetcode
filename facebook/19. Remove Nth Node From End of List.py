# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        r=l=head        
        distance=0
        while r.next:
            r=r.next
            distance+=1
            if distance==n:
                l=head
            elif distance>n:
                l=l.next
        
        #left pointer does not move, means remove first node
        if l==head:
            return head.next
        
        l.next = l.next.next
        return head

        
        
        
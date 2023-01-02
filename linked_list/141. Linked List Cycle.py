# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
There is a cycle in a linked list if there is some node in the list that can be reached again by 
continuously following the next pointer. Internally, pos is used to denote the index of the node 
that tail's next pointer is connected to. Note that pos is not passed as a parameter.
'''
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:        
        if head == None or head.next == None:
            return False        
        slow, fast = head.next, head.next.next
        
        while fast!=None and slow!=None:
            if fast == slow:
                return True            
            if fast.next == None:
                return False
            slow = slow.next            
            fast = fast.next.next
            
        return False
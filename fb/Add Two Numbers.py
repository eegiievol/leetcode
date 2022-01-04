# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:        
        def adder(l1, l2, add):
            if not l1 and not l2:
                if add:
                    return ListNode(add, None)                     
                else:
                    return None
            if not l1:
                val = l2.val+add
                l2.val = val%10
                l2.next = adder(None, l2.next, val//10)
                return l2
            if not l2:                
                val = l1.val+add                
                l1.val = val%10
                l1.next = adder(l1.next, None, val//10)
                return l1
            
            val = l1.val+l2.val+add
            l1.val = (val)%10
            l1.next = adder(l1.next, l2.next, (val//10))
            return l1
        
        return adder(l1, l2, 0)

        
                
    
        
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

# Example 1:


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
        
        def helper(l1, l2, carry):
            if not l1 and not l2:
                if carry:
                    return ListNode(carry, None)
                else:
                    return None
            if not l1:
                summ = l2.val + carry
                l2.val = summ%10
                carry = summ//10
                l2.next = helper(None, l2.next, carry)
                return l2
            if not l2:
                summ = l1.val + carry
                l1.val = summ%10
                carry = summ//10
                l1.next = helper(None, l1.next, carry)
                return l1
            
            summ = l1.val+l2.val+carry
            l1.val = summ%10
            l1.next = helper(l1.next, l2.next, summ//10)
            return l1
        
        return helper(l1,l2,0)

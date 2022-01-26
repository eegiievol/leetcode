# Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

# You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

 

# Example 1:

# Input: num1 = "11", num2 = "123"
# Output: "134"

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num2)>len(num1):
            return self.addStrings(num2, num1)  
        
        s1 = num1[::-1]
        s2 = num2[::-1]        
        ans = 0
        carry = 0
        digit = 1
        for i in range(len(s1)):
            if i<len(s2):
                sm = ord(s1[i])-ord('0')+ord(s2[i])-ord('0')+carry
                
            else:
                sm = ord(s1[i])-ord('0')+carry
                
            ans = ans + (sm%10)*digit
            carry = sm//10
            digit*=10
            
        if carry>0:
            print("left")
            ans+=carry*digit
        
        return str(ans)

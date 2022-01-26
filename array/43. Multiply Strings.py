# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

# Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

 

# Example 1:

# Input: num1 = "2", num2 = "3"
# Output: "6"

class Solution:
    #EEGII: Using Elementary math
    def multiply(self, num1: str, num2: str) -> str:        
        num1,num2 = list(num1), list(num2)        
        total = 0         
        level = 1
        for n2 in num2[::-1]:
            n2=int(n2)
            carry=0   
            ans = 0
            d = 1 
            for n1 in num1[::-1]:
                n1=int(n1)
                ans += (n2*n1+carry)%10*d
                carry = (n2*n1+carry)//10                
                d*=10
            ans += carry*d           
                       
            total += ans*level
            level*=10            
        return str(total)

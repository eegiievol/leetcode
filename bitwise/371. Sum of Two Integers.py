# Given two integers a and b, return the sum of the two integers without using the operators + and -.

class Solution:
    def getSum(self, a: int, b: int) -> int:        
        if abs(b)>abs(a):
            return self.getSum(b,a)    
                
        if a*b==0:
            return a
        x,y = abs(a), abs(b)
        
        sign = 1 if a > 0 else -1
        
        if a*b>0: #both negative or both positive
            while y:
                x,y = x^y, (x&y)<<1
        else: #subtract
            while y:
                x,y  = x^y, ((~x)&y)<<1
        
        return x*sign
                
            
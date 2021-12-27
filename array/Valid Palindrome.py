# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters 
# and removing all non-alphanumeric characters, it reads the same forward and backward. 
# Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

class Solution:
    def isPalindrome(self, s: str) -> bool:           
        def isAlphabet(numeric):
            if lbound<=numeric<=lbound+25:
                return True            
            if hbound<=numeric<=hbound+25:
                return True           
            return False        
            
        diff = abs(ord('a') - ord('A'))
        lbound = ord('a')
        hbound = ord('A')
        
        l,r = 0,len(s)-1
        while l<r:            
            while l<r and not s[l].isalnum(): #is alpha numeric
                l+=1
            while l<r and not s[r].isalnum():
                r-=1
                
            lch,rch = ord(s[l]), ord(s[r])
            if lch==rch:
                l+=1
                r-=1
            elif isAlphabet(lch) and isAlphabet(rch) and abs(lch-rch)==diff:                
                l+=1
                r-=1
            else:
                return False
            
        return True
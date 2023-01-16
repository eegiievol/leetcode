# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

 

# Example 1:

# Input: s = "aba"
# Output: true

class Solution:
    def validPalindrome(self, s: str) -> bool:        
        def findpal(l,r):            
            while l<r:
                if s[l]==s[r]:
                    l+=1
                    r-=1          
                else:
                    if not self.isDeleted:
                        self.isDeleted=True
                        return findpal(l+1, r) or findpal(l, r-1)
                    else:
                        return False            
            return True
        
        self.isDeleted=False
        return findpal(0, len(s)-1)

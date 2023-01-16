# Given two strings s and t, return true if they are both one edit distance apart, otherwise return false.

# A string s is said to be one distance apart from a string t if you can:

# Insert exactly one character into s to get t.
# Delete exactly one character from s to get t.
# Replace exactly one character of s with a different character to get t.

class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        slen, tlen = len(s), len(t)      
        i,j=0,0
        diff=0  
        
        if abs(slen-tlen)>1:
            return False  
        
        while i<slen and j<tlen:
            if s[i]!=t[j]:
                diff+=1
                if slen>tlen and i+1<slen and s[i+1]==t[j]:
                    i+=1
                elif tlen>slen and j+1<tlen and t[j+1]==s[i]:
                    j+=1              
            i+=1
            j+=1               
        
        if diff+max(slen-i, tlen-j)!=1:
            return False
            
        return True
            
# Given two strings text1 and text2, return the length of their longest common subsequence. 
# If there is no common subsequence, return 0.

# A subsequence of a string is a new string generated from the original string with some 
# characters (can be none) deleted without changing the relative order of the remaining 
# characters.

# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        def dp(i,j):
            if i==m or j==n:
                return 0            
            if (i,j) in mem:
                return mem[(i,j)]              
            #longest substr does NOT includes text1[i]  
            wo_i = dp(i+1,j)
            
            #longest substr includes text1[i]
            #this case, we find first occurence of text1[i] in text2
            jj=j
            while jj<n: 
                if text2[jj]==text1[i]:
                    break
                jj+=1
            if jj==n:
                wi_i=0                
            else:
                wi_i = dp(i+1, jj+1)+1             
            
            mx = max(wi_i, wo_i)
            mem[(i,j)]=mx
            return mx
        
        mem = {}
        m,n=len(text1),len(text2)
        return dp(0,0)


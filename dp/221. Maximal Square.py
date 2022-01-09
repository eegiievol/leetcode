#Given an m x n binary matrix filled with 0's and 1's, 
#find the largest square containing only 1's and return its area.

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int: 
        def dp(i,j): #dp(i,j) returns biggest square size whose bottom right corner is (i,j)
            if i>m or i<0 or j>n or j<0:
                return 0           
            if matrix[i][j] == '0':
                return 0
            
            if (i,j) in mem:
                return mem[(i,j)]
            #check left,top,top-left sub squares            
            sm = min(dp(i-1,j), dp(i-1,j-1), dp(i,j-1)) + 1
            mem[(i,j)]=sm
            return sm
                
        ans=0
        mem = {}
        m,n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                ans=max(ans,dp(i,j))
        return ans*ans
        
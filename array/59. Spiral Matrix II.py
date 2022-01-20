# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

 

# Example 1:


# Input: n = 3
# Output: [[1,2,3],[8,9,4],[7,6,5]]

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0]* n for _ in range(n)]
        
        ctr = 1
        rang = (n+1)//2
        for d in range(rang):
            r=d
            for c in range(d, n-d-1):
                ans[r][c] = ctr
                ctr+=1
            c=n-1-d
            for r in range(d, n-d-1):
                ans[r][c] = ctr
                ctr+=1
            r=n-1-d
            for c in range(n-d-1, d, -1):
                ans[r][c] = ctr
                ctr+=1
            c=d
            for r in range(n-d-1, d, -1):
                ans[r][c] = ctr
                ctr+=1    
        if n%2:
            ans[n//2][n//2] = ctr
                
        return ans

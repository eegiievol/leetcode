# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
 
# Example 1:
# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(0,1), (1,0), (0,-1), (-1,0)]      
        q=deque()        
        rowsize,colsize = len(grid), len(grid[0])        
        fresh=0
        for row in range(rowsize):
            for col in range(colsize):
                if grid[row][col]==2:
                    q.append((row,col))
                elif grid[row][col]==1:
                    fresh+=1
        if fresh==0:
            return 0        
        ans = -1
        while q:
            size = len(q)
            ans+=1
            for _ in range(size):
                r,c = q.popleft()  
                for ro,co in directions:
                    row, col = r+ro, c+co
                    if 0<=row<rowsize and 0<=col<colsize and grid[row][col]==1:
                        grid[row][col]=2
                        q.append((row, col))
                        fresh-=1           
        return ans if fresh==0 else -1
                    
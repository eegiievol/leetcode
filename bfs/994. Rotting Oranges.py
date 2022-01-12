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
        q=deque()
        fresh = 0
        rowsize, colsize= len(grid), len(grid[0])
        for row in range(rowsize):
            for col in range(colsize):
                if grid[row][col]==1:
                    fresh +=1
                if grid[row][col]==2:
                    q.append((row,col)) #add rottens to queue
        if fresh==0:
            return 0
        
        directions = ((0,1),(1,0),(0,-1),(-1,0))
        rotten = 0
        minutes = -1
        
        while q:
            size = len(q)
            for _ in range(size):
                row,col = q.popleft()   
                for d in directions:
                    newr,newc = row+d[0], col+d[1]
                    if 0<=newr<rowsize and 0<=newc<colsize and grid[newr][newc]==1:
                        rotten+=1
                        grid[newr][newc]=2
                        q.append((newr, newc))
            minutes+=1
        
        return minutes if rotten==fresh else -1

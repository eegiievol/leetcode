# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
 
# Example 1:
# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
import collections
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        rowlen, collen = len(grid), len(grid[0])
        fresh = 0

        for i in range(rowlen):
            for j in range(collen):
                if grid[i][j]==2:
                    q.append((i,j))
                elif grid[i][j]==1:
                    fresh += 1
        if fresh==0:
            return 0

        minute = -1
        while q:
            minute += 1
            for _ in range(len(q)):
                r,c = q.popleft()
                for nr, nc in [(0,1),(1,0),(-1,0),(0,-1)]:
                    newrow, newcol = r+nr, c+nc
                    if 0<=newrow<rowlen and 0<=newcol<collen and grid[newrow][newcol]==1:
                        grid[newrow][newcol] = 2
                        fresh -=1
                        q.append((newrow,newcol))
        
        return minute if fresh==0 else -1

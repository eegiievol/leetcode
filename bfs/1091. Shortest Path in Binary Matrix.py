# Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

# A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

# All the visited cells of the path are 0.
# All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
# The length of a clear path is the number of visited cells of this path.
# test

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        maxr,maxc=len(grid),len(grid[0])
        if grid[0][0]!=0 or grid[maxr-1][maxc-1]!=0:
            return -1
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]        
        visited = [[0]*maxc for _ in range(maxr)]       

        q=deque()
        q.append((0,0))
        ans = 0
        level = {(0,0):1}
        while q:
            r,c=q.popleft()
            if r==maxr-1 and c==maxc-1:
                return level[(r,c)]
            for ro,co in directions:                
                nr,nc = r+ro, c+co
                if 0<=nr<maxr and 0<=nc<maxc and grid[nr][nc]==0 and visited[nr][nc]==0:
                    nei = (nr,nc)
                    q.append(nei)
                    level[nei]=level[(r,c)]+1
                    visited[nr][nc]=1
        return -1  
              
        


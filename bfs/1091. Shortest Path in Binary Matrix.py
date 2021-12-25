# Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

# A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

# All the visited cells of the path are 0.
# All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
# The length of a clear path is the number of visited cells of this path.


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n=len(grid)
        if n==0:
            return -1        
        length={(0,0):1}        
        mat = defaultdict(list)
        visited={}
        q=deque()        
        for r in range(n):
            for c in range(n):
                if grid[r][c]!=0:
                    continue
                #building neighbords list
                for i in range(r-1,r+2):
                    for j in range(c-1,c+2):
                        if (i,j)==(r,c):
                            continue
                        if 0<=i<n and 0<=j<n and grid[i][j]==0:
                            mat[(r,c)].append((i,j))              
        visited[(0,0)]=1
        q.append((0,0))
        
        while q:
            i,j = q.popleft()            
            if i==n-1 and j==n-1:
                return length[(i,j)]
            for nei in mat[(i,j)]:                
                ni, nj = nei[0], nei[1]
                if (ni,nj) not in visited:
                    q.append((ni,nj))
                    visited[(ni,nj)]=True
                    length[(ni,nj)]=length[(i,j)]+1
        return -1
                            
        


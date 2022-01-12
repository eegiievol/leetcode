# Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

# The distance between two adjacent cells is 1.

 

# Example 1:


# Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
# Output: [[0,0,0],[0,1,0],[0,0,0]]

#####################################################################
# Algorithm

# For our BFS routine, we keep a queue, q to maintain the queue of cells to be examined next.
# We start by adding all the cells with 0s to q.
# Intially, distance for each 0 cell is 0 and distance for each 1 is INT_MAX, which is updated during the BFS.
# Pop the cell from queue, and examine its neighbors. If the new calculated distance for neighbor {i,j} is smaller, we add {i,j} to q and update dist[i][j].

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rowsize, colsize = len(mat), len(mat[0])
        dist = [[float('inf')] * colsize for _ in range(rowsize)]                
        q=deque()
        for row in range(rowsize):
            for col in range(colsize):
                if mat[row][col]==0:
                    dist[row][col]=0
                    q.append((row,col))
                    
        directions = ((0,1), (1,0), (-1,0), (0,-1))
        q.append((row,col))
        while q:
            r, c = q.popleft()
            for ro,co in directions:
                newrow = r+ro
                newcol = c+co
                if 0<=newrow<rowsize and 0<=newcol<colsize:
                    #check if neighbor distance can be updated
                    if dist[newrow][newcol] > dist[r][c]+1: 
                        dist[newrow][newcol] = dist[r][c]+1
                        q.append((newrow, newcol))
        return dist

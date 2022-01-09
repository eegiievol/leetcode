# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

# The area of an island is the number of cells with a value 1 in the island.

# Return the maximum area of an island in grid. If there is no island, return 0.

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(r,c):
            if r<0 or r>=rowlen:
                return 0
            if c<0 or c>=collen:
                return 0
            if grid[r][c]==0 or visited[(r,c)]==1:
                return 0            
            visited[(r,c)]=1            
            return dfs(r+1,c)+dfs(r,c+1)+dfs(r-1,c)+dfs(r,c-1)+1
            
        visited = {(rr,cc):0 for rr in range(len(grid)) for cc in range(len(grid[0]))}
        
        rowlen=len(grid)
        collen=len(grid[0])
        ans = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]==1 and visited[(row,col)]==0:
                    ans = max(ans, dfs(row,col))
        
        return ans

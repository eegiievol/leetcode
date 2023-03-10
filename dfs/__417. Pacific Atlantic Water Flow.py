'''
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, 
and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above 
sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's 
height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and 
Atlantic oceans.
'''
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        def dfs(r,c,reach_ocean):
            reach_ocean.add((r,c))
            for ro,co in [[0,1],[1,0],[-1,0],[0,-1]]:
                newrow, newcol = r+ro, c+co
                if 0<=newrow<m and 0<=newcol<n \
                        and heights[newrow][newcol] >= heights[r][c] \
                        and (newrow, newcol) not in reach_ocean:
                    dfs(newrow, newcol, reach_ocean)

        m, n = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        for i in range(m):
            dfs(i,0,pacific)
            dfs(i,n-1,atlantic)

        for i in range(n):
            dfs(0,i,pacific)
            dfs(m-1,i,atlantic)
      
        return list(atlantic.intersection(pacific))





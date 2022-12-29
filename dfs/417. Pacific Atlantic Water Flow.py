'''
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.
'''
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def dfs(row, col, reachable):
            reachable.add((row,col))
            for x,y in [(1,0),(0,1),(-1,0),(0,-1)]:
                newrow, newcol = row+x, col+y
                if newrow<0 or newcol<0 or newrow>=height or newcol>=width:
                    continue
                if (newrow, newcol) in reachable:
                    continue

                if heights[newrow][newcol] >= heights[row][col]:
                    dfs(newrow, newcol, reachable)


        ans = []
        reach_pac, reach_atl = set(), set()
        height, width = len(heights), len(heights[0])

        for i in range(height):
            dfs(i, 0, reach_pac)
            dfs(i, width-1, reach_atl)

        for i in range(width):
            dfs(0, i, reach_pac)
            dfs(height-1, i, reach_atl)

        return reach_atl.intersection(reach_pac)

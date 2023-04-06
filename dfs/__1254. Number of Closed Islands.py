'''
Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.

 

Example 1:



Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output: 2
Explanation: 
Islands in gray are closed because they are completely surrounded by water (group of 1s).
Example 2:



Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
Output: 1
Example 3:

Input: grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
Output: 2
 
'''
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rowlen or c >= collen:
                return False

            if grid[r][c] == 1:
                return True

            visited.add((r, c))
            res = True
            for ro,co in [(1,0),(0,1),(-1,0),(0,-1)]:
                newrow, newcol = ro+r, co+c
                if (newrow, newcol) not in visited and not dfs(newrow, newcol):
                    res = False
            return res

        visited = set()
        rowlen, collen = len(grid), len(grid[0])

        ans = 0
        for i in range(rowlen):
            for j in range(collen):
                if grid[i][j] == 0 and (i,j) not in visited and dfs(i,j):
                    ans += 1
        return ans

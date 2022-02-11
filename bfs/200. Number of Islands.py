
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:        
        def bfs(row,col): 
            directions = [(0,1),(1,0),(-1,0),(0,-1)]
            q=deque()
            q.append((row,col))
            while q:
                r,c = q.popleft()
                if (r,c) in visited:
                    continue
                visited.add((r,c))
                for dr,dc in directions:
                    ro,co = r+dr, c+dc
                    if 0<=ro<len(grid) and 0<=co<len(grid[0]) and grid[ro][co]=='1':
                        q.append((ro,co))
        
        visited = set()
        ans = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]=='1' and (row,col) not in visited:
                    ans+=1
                    bfs(row,col)
        return ans
                    
                    
        

                
                    
    
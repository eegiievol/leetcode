
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
        def bfs(neis, comps, compnum, node):
            q = deque()
            visited = []
            q.append(node)
            while q:
                popped = q.popleft()
                comps[popped] = compnum
                for nei in neis[popped]:
                    if nei not in visited:
                        visited.append(nei)
                        q.append(nei)            
        
        #register neighbors
        directions = [(0,-1), (0,1), (1,0), (-1,0)]
        neis = defaultdict(list)
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]=='1':
                    for d in directions:
                        r = row+d[0]
                        c = col+d[1]
                        if 0<=r<len(grid) and 0<=c<len(grid[0]) and grid[r][c]=='1':
                            neis[(row,col)].append((r,c))
                            
        #do bfs and register nodes into connected components
        comps = {}
        compnum = 1
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]=='1':                    
                    if (row,col) in comps:
                        continue
                    else:
                        bfs(neis, comps, compnum, (row,col))
                        compnum+=1
                        
        return max(comps.values()) if len(comps)>0 else 0

                
                    
    
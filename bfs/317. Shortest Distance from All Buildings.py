class Solution:
    def __init__(self):
            self.traps={}
    def shortestDistance(self, grid: List[List[int]]) -> int: 
        def bfs(start, grid, mat, bld_count):
            steps=0
            distance={start:0} 
            visited=[]
            bld_visited=0 #visited buildings so far
            
            q=deque()
            q.append(start)
            while q:
                popped=q.popleft()
                r,c=popped                
                if grid[r][c]==1:
                    bld_visited+=1
                    steps+=distance[popped]
                if bld_visited==bld_count:
                    return steps
                for nei in mat[popped]:                    
                    if nei not in visited:
                        q.append(nei)
                        visited.append(nei)
                        distance[nei] = distance[popped]+1
            
            #reach here means couldnt reach all houses
            #so we mark all visited node as traps
            for i in visited:
                grid[i[0]][i[1]]==2            
            return float('inf')            
        
        row,col = len(grid),len(grid[0])
        mat = defaultdict(list)
        bld_count=0
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        for r in range(row):
            for c in range(col):
                if grid[r][c]==0:
                    for d in dirs:
                        if 0<=r+d[0]<row and 0<=c+d[1]<col:
                            mat[(r,c)].append((r+d[0],c+d[1]))                        
                if grid[r][c]==1:
                    bld_count+=1
        
        ans = float('inf')
        for r in range(row):
            for c in range(col):
                if grid[r][c]==0:                    
                    ans = min(ans, bfs((r,c), grid, mat, bld_count))                
        return -1 if ans==float('inf') else ans
        
            
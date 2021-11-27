class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:        
        
        '''
        #BFS
        ans = []
        q = deque()
        target = len(graph)-1
        
        q.append([0])
        
        while q:
            popped = q.popleft()
            for neighbor in graph[popped[-1]]:
                path = popped + [neighbor]
                if neighbor == target:
                    ans.append(path)
                else:
                    q.append(path)
        return ans
        '''        
        
        #DFS        
        def dfs(path, node):           
            visited[node]=True
            for nei in graph[node]:
                if nei==target:
                    ans.append(path+[nei])
                if visited[nei]==False:
                    dfs(path+[nei], nei)
            visited[node]=False
            return
            
        
        ans = []         
        target = len(graph)-1
        visited = [False]*(target+1)
        
        dfs([0], 0)
        return ans
            
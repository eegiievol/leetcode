class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:

        mat = defaultdict(dict)
        for i,j in edges:
            mat[i][j]=1
            mat[j][i]=1

        visited = [False]*n

        stack = [start]
        visited[start]=True

        while stack:
            popped = stack.pop()
            if popped==end:
                return True

            for nei in mat[popped]:
                if visited[nei]==False:
                    stack.append(nei)
                    visited[nei]=True
        return False

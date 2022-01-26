# You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

# Return true if the edges of the given graph make up a valid tree, and false otherwise.

 

# Example 1:


# Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
# Output: true

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        def find(v):
            while parent[v]!=v:
                v=parent[v]
            return v        
        def union(v1,v2):
            r1,r2 = find(v1), find(v2)
            if r1==r2:
                return False
            
            if height[r1]==height[r2]:
                height[r1]+=1
                parent[r2]=r1
            elif height[r1]>height[r2]:
                parent[r2]=r1
            else:
                parent[r1]=r2            
            return True    
        
        if not edges:
            if n == 1:
                return True 
            else:
                return False 
        if len(edges)<n-1:
            return False
        
        height , parent = {}, {}
        for n in range(n):
            height[n] = 0
            parent[n]=n
        
        for v1,v2 in edges:
            if not union(v1,v2):
                return False
           
        #check if there are more than 1 connected components
        components = []
        for node in range(n):
            root = find(node)
            if root not in components:
                components.append(root)
            if len(components)>1:
                return False
        
        return True
            
            
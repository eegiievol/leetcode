# There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.
# A province is a group of directly or indirectly connected cities and no other cities outside of the group.
# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.
# Return the total number of provinces.

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:        
        def findroot(node):            
            while parent[node]!=node:
                node = parent[node]
            return node
        
        def union(a, b):
            root_a = findroot(a)
            root_b = findroot(b)
            if height[root_a]==height[root_b]:
                height[root_a]+=1
                parent[root_b] = root_a             
            elif height[root_a]>height[root_b]:
                parent[root_b] = root_a  
            else:
                parent[root_a] = root_b
        
        parent = {node:node for node in range(len(isConnected))}
        height = [0]*len(isConnected)
        
        for i in range(len(isConnected)-1):
            for j in range(i+1, len(isConnected)): 
                if isConnected[i][j]==1:
                    union(i,j)      
                    
        disjoints = {}
        for i in range(len(isConnected)):
            root = findroot(i)
            disjoints[root] = disjoints.get(root, 1)
        
        return len(disjoints)


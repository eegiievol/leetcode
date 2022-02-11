# There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.
# A province is a group of directly or indirectly connected cities and no other cities outside of the group.
# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.
# Return the total number of provinces.

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:        
        def find(node):
            if head[node]==node:
                return node
            head[node] = find(head[node])
            return head[node]
        def union(n1,n2):
            nonlocal components
            r1,r2 = find(n1), find(n2)
            if r1!=r2:
                components -= 1
                head[r2]=r1

        head = [i for i in range(len(isConnected))]
        components = len(isConnected) 
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if i!=j and isConnected[i][j]==1:
                    union(i, j)
        return components
    

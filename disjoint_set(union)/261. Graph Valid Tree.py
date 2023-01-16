# You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

# Return true if the edges of the given graph make up a valid tree, and false otherwise.

 

# Example 1:


# Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
# Output: true

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #union find
        def find(node):
            if self.root[node]==node:
                return node
            self.root[node] = find(self.root[node]) 
            return self.root[node]
        def union(n1, n2):
            r1, r2 = find(n1), find(n2)
            if r1==r2:
                return False #detect loop
            if self.height[r1]>self.height[r2]:
                self.root[r2] = r1
                self.height[r1] += 1
            else:
                self.root[r1] = r2
                self.height[r2] += 1
            self.union_sets -=1

            return True
        
        self.height = [0 for i in range(n)]
        self.root = [i for i in range(n)]
        self.union_sets = n

        for v1,v2 in edges:
            if not union(v1,v2):
                return False

        return self.union_sets==1
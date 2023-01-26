# You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

# Return true if the edges of the given graph make up a valid tree, and false otherwise.

 

# Example 1:


# Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
# Output: true

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        def find(node):
            if root[node] == node:
                return node
            root[node] = find(root[node])
            return root[node]

        def union(n1, n2):
            r1, r2 = find(n1), find(n2)
            if r1 != r2:
                self.sets -= 1
                root[r1] = r2

        root = [i for i in range(n)]
        self.sets = n
        for s,d in edges:
            union(s, d)
        
        return self.sets == 1 and len(edges)==n-1

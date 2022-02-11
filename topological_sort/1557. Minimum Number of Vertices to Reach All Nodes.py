# Given a directed acyclic graph, with n vertices numbered from 0 to n-1, and an array edges where edges[i] = [fromi, toi] represents a directed edge from node fromi to node toi.

# Find the smallest set of vertices from which all nodes in the graph are reachable. It's guaranteed that a unique solution exists.

# Notice that you can return the vertices in any order.

 

# Example 1:



# Input: n = 6, edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]
# Output: [0,3]
# Explanation: It's not possible to reach all the nodes from a single vertex. From 0 we can reach [0,1,2,5]. From 3 we can reach [3,4,2,5]. So we output [0,3].
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:      
        indegree = {node: 0 for node in range(n)}
        for s,d in edges:
            indegree[d] += 1
        ans = []
        for d in indegree:
            if indegree[d]==0:
                ans.append(d)
        return ans
        

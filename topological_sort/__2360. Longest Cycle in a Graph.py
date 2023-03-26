'''
You are given a directed graph of n nodes numbered from 0 to n - 1, where each node has at most one outgoing edge.

The graph is represented with a given 0-indexed array edges of size n, indicating that there is a directed edge from node i to node edges[i]. If there is no outgoing edge from node i, then edges[i] == -1.

Return the length of the longest cycle in the graph. If no cycle exists, return -1.

A cycle is a path that starts and ends at the same node.

 

Example 1:


Input: edges = [3,3,4,2,3]
Output: 3
Explanation: The longest cycle in the graph is the cycle: 2 -> 4 -> 3 -> 2.
The length of this cycle is 3, so 3 is returned.
Example 2:


Input: edges = [2,-1,3,1]
Output: -1
Explanation: There are no cycles in this graph.
 
'''

class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        #do topological sort (Khan)
        #mark visited nodes. 
        #nodes in a cycle cannot be visited in Khan's algo
        indegree = [0 for _ in range(n)]
        for i in range(n):
            if edges[i]>=0:
                indegree[edges[i]] += 1
        q = deque()
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)

        visited = [0 for i in range(n)]
        while q:
            popped = q.popleft()
            visited[popped] = 1
            nei = edges[popped]
            if nei>=0:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        #dfs on connected components
        ans = 0
        count = 0
        for i in range(n):
            count = 0
            if not visited[i]:
                cur = i
                while cur>=0:
                    if visited[cur]:
                        break
                    visited[cur] = 1
                    count +=1
                    cur = edges[cur]
                ans = max(ans, count)
        
        return ans if ans else -1

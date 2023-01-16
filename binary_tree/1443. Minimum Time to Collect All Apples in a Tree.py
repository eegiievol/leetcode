'''
Given an undirected tree consisting of n vertices numbered from 0 to n-1, which has some apples in their vertices. You spend 1 second to walk over one edge of the tree. Return the minimum time in seconds you have to spend to collect all apples in the tree, starting at vertex 0 and coming back to this vertex.

The edges of the undirected tree are given in the array edges, where edges[i] = [ai, bi] means that exists an edge connecting the vertices ai and bi. Additionally, there is a boolean array hasApple, where hasApple[i] = true means that vertex i has an apple; otherwise, it does not have any apple.

 

Example 1:


Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,true,true,false]
Output: 8 
Explanation: The figure above represents the given tree where red vertices have an apple. One optimal path to collect all apples is shown by the green arrows.  
'''

import collections
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        def dfs(root):
            visited.add(root)
            val = 0
            for child in neighbor[root]:
                if child not in visited:
                    val += dfs(child)
            if not val:
                val = hasApple[root]
            else:
                val += 1
            return val        
        
        visited = set()
        neighbor = collections.defaultdict(list)
        for parent, child in edges:
            neighbor[parent].append(child)
            neighbor[child].append(parent)
        ans = dfs(edges[0][0]) 
        return (ans-1)*2 if ans else 0
            

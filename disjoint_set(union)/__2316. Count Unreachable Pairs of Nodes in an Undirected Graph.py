'''
You are given an integer n. There is an undirected graph with n nodes, numbered from 0 to n - 1. 
You are given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an 
undirected edge connecting nodes ai and bi.

Return the number of pairs of different nodes that are unreachable from each other.

 

Example 1:


Input: n = 3, edges = [[0,1],[0,2],[1,2]]
Output: 0
Explanation: There are no pairs of nodes that are unreachable from each other. Therefore, we return 0.
Example 2:


Input: n = 7, edges = [[0,2],[0,5],[2,4],[1,6],[5,4]]
Output: 14
Explanation: There are 14 pairs of nodes that are unreachable from each other:
[[0,1],[0,3],[0,6],[1,2],[1,3],[1,4],[1,5],[2,3],[2,6],[3,4],[3,5],[3,6],[4,6],[5,6]].
Therefore, we return 14.
 
'''
class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:

        def find(node):
            if root[node] == node:
                return node
            root[node] = find(root[node])
            return root[node]
        def union(n1, n2):
            r1, r2 = find(n1), find(n2)
            if r1!=r2:
                root[r1] = r2
    
        #find union
        root = [i for i in range(n)]
        for s,d in edges:
            union(s,d)
        
        #group nodes by their root
        unions_reg = defaultdict(list)
        for node in range(n):
            r = find(node)
            unions_reg[r].append(node)
        
        #put number of nodes in unions into list
        union_list = [len(unions_reg[key]) for key in unions_reg]
        
        #count unreachable pairs 
        ans = 0
        prev = union_list[0]
        for i in range(1, len(union_list)):
            ans += prev * union_list[i]
            prev += union_list[i] 
        
        return ans

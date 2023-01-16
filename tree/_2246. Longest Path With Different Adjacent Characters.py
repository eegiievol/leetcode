'''
You are given a tree (i.e. a connected, undirected graph that has no cycles) rooted at node 0 consisting of n nodes 
numbered from 0 to n - 1. The tree is represented by a 0-indexed array parent of size n, where parent[i] is the 
parent of node i. Since node 0 is the root, parent[0] == -1.

You are also given a string s of length n, where s[i] is the character assigned to node i.

Return the length of the longest path in the tree such that no pair of adjacent nodes on the path have the same 
character assigned to them.

Example 1:
Input: parent = [-1,0,0,1,1,2], s = "abacbe"
Output: 3
Explanation: The longest path where each two adjacent nodes have different characters in the tree is the path: 0 -> 1 -> 3. 
The length of this path is 3, so 3 is returned.
It can be proven that there is no longer path that satisfies the conditions. 

Example 2:
Input: parent = [-1,0,0,0], s = "aabc"
Output: 3
Explanation: The longest path where each two adjacent nodes have different characters is the path: 2 -> 0 -> 3. 
The length of this path is 3, so 3 is returned.
'''
import heapq
class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        def dfs(root):
            heap = []
            for child in self.children[root]:
                r = dfs(child)
                if s[child] != s[root]:
                    heapq.heappush(heap, -r)
                    
            #in case longest path root is current node
            longest = second_longest = 0

            if heap:
                longest = -heapq.heappop(heap)
            if heap:
                second_longest = -heapq.heappop(heap)
            self.ans = max(self.ans, longest + second_longest+1)

            #in case longest path is root is not current node
            return longest + 1

        self.children = collections.defaultdict(list)
        for child, parent in enumerate(parent):
            if parent >= 0:
                self.children[parent].append(child)

        self.ans = 0
        dfs(0)
        return self.ans

    
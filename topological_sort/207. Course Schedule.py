# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

 

# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.

#SOLUTION 1: Grey Node Algorithm for Cycle detect
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:        
        def dfs(node):
            if status[node]==1: #grey node
                return False
            if status[node]==2:
                return True
            
            status[node]=1
            for nei in neighbors[node]:
                if not dfs(nei):
                    return False
            status[node]=2
            return True
        
        status = {i:0 for i in range(numCourses)}
        neighbors = defaultdict(list)
        for c,p in prerequisites:
            neighbors[p].append(c)
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

#SOLUTION 2: Topological sort algorithm for Cycle detect
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        neighbors = defaultdict(list)
        indegree = [0 for _ in range(numCourses)]
        for c,p in prerequisites:
            indegree[c] += 1
            neighbors[p].append(c)
        q = deque()
        for c in range(numCourses):
            if indegree[c]==0: q.append(c)
        
        #topological sort algorithm
        coursesTaken = 0
        while q:
            course = q.popleft()
            coursesTaken += 1
            for nei in neighbors[course]:
                indegree[nei] -= 1
                if indegree[nei] == 0: 
                    q.append(nei)
        
        return True if coursesTaken == numCourses else False

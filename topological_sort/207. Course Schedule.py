# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

 

# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:        
        indegree = [0 for _ in range(numCourses)]
        adj_list = defaultdict(list)
        
        for s,d in prerequisites:
            indegree[d]+=1
            adj_list[s].append(d)   
        
        q = deque()
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
                
        order = []
        while q:
            popped = q.popleft()
            order.append(popped)
            for nei in adj_list[popped]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        
        return True if len(order)==numCourses else False

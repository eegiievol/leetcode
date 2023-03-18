# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

 

# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0 for _ in range(numCourses)]
        neighbors = defaultdict(list)

        for d,s in prerequisites:
            neighbors[s].append(d)
            indegree[d] += 1
        
        q = deque()
        [q.append(i) for i in range(numCourses) if indegree[i] == 0]
        ans = []

        taken = 0
        while q:
            popped = q.popleft()
            ans.append(popped)
            for nei in neighbors[popped]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return ans if len(ans) == numCourses else []

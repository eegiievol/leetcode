# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

 

# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def doTopologicalSort(q, numCourses):
            topsort = []            
            while q:
                node = q.popleft()                
                for nei in hmap[node]:
                    inc[nei]-=1
                    if inc[nei]==0:
                        q.append(nei)
                topsort.append(node)         
            #if we cant topological sort all nodes, there is a CYCLE
            return topsort if len(topsort)==numCourses else []             
        
        hmap = defaultdict(list)
        inc = {} #incoming edge count        
        for d,s in prerequisites:
            hmap[s].append(d)
            inc[d] = inc.get(d, 0) + 1
            
        #if there are nodes with no incoming edges, add it to queue        
        q = deque()
        for node in range(numCourses):
            if node not in inc:
                q.append(node)        
        return doTopologicalSort(q, numCourses)

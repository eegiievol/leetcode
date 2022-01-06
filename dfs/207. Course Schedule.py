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
        def dfs(node):            
            if stat[node]==1:
                stat[node]=2
                return False  
            
            if stat[node]==2: #black node
                return True            
            if len(mat[node])==0: #means leaf node
                return True        
            stat[node]=1 #visiting node
            for nei in mat[node]:
                if not dfs(nei):
                    return False
            stat[node]=2 #processed node
            return True
        
        if not prerequisites:
            return True
        
        mat=defaultdict(list)
        stat={}
        for cour,preq in prerequisites:
            mat[preq].append(cour)        
        
        for node in range(numCourses):           
            stat[node]=0
        
        for node in range(numCourses):
            if not dfs(node):
                return False
        return True

'''
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, 
return the maximum number of points that lie on the same straight line.

Example 1:

Input: points = [[1,1],[2,2],[3,3]]
Output: 3

'''
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 1:
            return 1
        ans = 2
        for i in range(n):
            ctr = {}
            for j in range(n):
                if i != j:
                    atan = math.atan2(points[i][1]-points[j][1], \
                                points[i][0]-points[j][0])
                    ctr[atan] = ctr.get(atan, 0) + 1
            ans = max(ans, max(ctr.values())+1)
        
        return ans


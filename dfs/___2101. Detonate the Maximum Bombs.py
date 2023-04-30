'''
You are given a list of bombs. The range of a bomb is defined as the area where its effect can be felt. This area is in the shape of a circle with the center as the location of the bomb.

The bombs are represented by a 0-indexed 2D integer array bombs where bombs[i] = [xi, yi, ri]. xi and yi denote the X-coordinate and Y-coordinate of the location of the ith bomb, whereas ri denotes the radius of its range.

You may choose to detonate a single bomb. When a bomb is detonated, it will detonate all bombs that lie in its range. These bombs will further detonate the bombs that lie in their ranges.

Given the list of bombs, return the maximum number of bombs that can be detonated if you are allowed to detonate only one bomb.

 

Example 1:


Input: bombs = [[2,1,3],[6,1,4]]
Output: 2
Explanation:
The above figure shows the positions and ranges of the 2 bombs.
If we detonate the left bomb, the right bomb will not be affected.
But if we detonate the right bomb, both bombs will be detonated.
So the maximum bombs that can be detonated is max(1, 2) = 2.
Example 2:


Input: bombs = [[1,1,5],[10,10,5]]
Output: 1
Explanation:
Detonating either bomb will not detonate the other bomb, so the maximum number of bombs that can be detonated is 1.
'''
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:

        def canExplode(b1, b2):
            xdist = abs(b1[0]-b2[0]) 
            ydist = abs(b1[1]-b2[1]) 

            ans = 0
            dist = sqrt(xdist*xdist + ydist*ydist)
            if dist <= b1[2]:
                ans |= 1
            if dist <= b2[2]:
                ans |= 2
            return ans
        
        def dfs(node, visited, adj_list):
            total = 1
            for nei in adj_list[node]:
                if nei not in visited:
                    visited.add(nei)
                    total += dfs(nei, visited, adj_list)
            return total


        n = len(bombs)
        adj_list = defaultdict(list)
        for i in range(n-1):
            for j in range(i+1, n):
                r = canExplode(bombs[i], bombs[j])
                if r & 1:
                    adj_list[i].append(j)
                if r & 2:
                    adj_list[j].append(i)

        ans = 0
        for i in range(n):
            visited = set()
            visited.add(i)
            ans = max(ans, dfs(i, visited, adj_list))

        return ans

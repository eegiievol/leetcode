# You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

# The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

# Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.
 
# Example 1:
# Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
# Output: 20

#EEGII: APPLY PRIM'S ALGORITH TO DRAW MINIMUM SPANNING TREE, ACCUMULATE COST WHILE DOING SO.

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        leng=len(points)
        for i in range(leng-1):
            for j in range(i+1,leng):
                l=points[i]
                r=points[j]
                adj_list[(l[0], l[1])].append((r[0], r[1]))
                adj_list[(r[0], r[1])].append((l[0], l[1]))
            
        #add random node to heap
        random = (points[0][0],points[0][1])
        heap = [(0,random)]
        visited = []
        ans = 0
        
        while len(visited)<leng:
            cost, node = heappop(heap)
            if node in visited: 
                continue
            visited.append(node)
            ans += cost
            for nei in adj_list[node]:                                   
                c = abs(nei[1]-node[1]) + abs(nei[0]-node[0]) 
                heappush(heap, (c, nei))
        return ans

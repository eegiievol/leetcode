class Solution:
    
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:  
        #(cost, node, k)
        h=[(0, src, k+1)]  
        
        d = defaultdict(dict)
        for a,b,p in flights:
            d[a][b]=p
        
        while h: 
            c, cur, k = heappop(h)
            if cur == dst:
                return c
            if k>0:
                for j in d[cur]:
                    heapq.heappush(h, (c + d[cur][j], j, k - 1))
                        
        return -1
    
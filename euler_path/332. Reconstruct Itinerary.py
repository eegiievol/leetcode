'''
You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and 
the arrival airports of one flight. Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". 
If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical 
order when read as a single string.

For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.
'''

class Solution(object):
    def findItinerary(self, tickets):        
        
        def dfs(node):
            dests = mat[node]
            while dests:
                dest = dests.pop()
                dfs(dest)
            ans.append(node)
        
        mat = defaultdict(list)
        for s,d in tickets:
            mat[s].append(d)
        ans = []
        for s,dest in mat.items():
            dest.sort(reverse=True)
        dfs("JFK")
        
        return ans[::-1]
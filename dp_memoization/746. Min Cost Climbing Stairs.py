# You are given an integer array cost where cost[i] is the 
# cost of ith step on a staircase. Once you pay the cost, 
# you can either climb one or two steps.

# You can either start from the step with index 0, or the 
# step with index 1.

# Return the minimum cost to reach the top of the floor.

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def helper(cost, mem, n):                  
            if n<2:
                return cost[n]            
            if n in mem:
                return mem[n]         
            optimal = min(helper(cost, mem, n-1), helper(cost, mem, n-2)) + cost[n]
            mem[n] = optimal
            return optimal  
        
        cost.append(0) #step to roof cost = 0
        top = len(cost)-1
        mem = {}
        return helper(cost, mem, top)
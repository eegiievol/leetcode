# You are a professional robber planning to rob houses along a street. 
# Each house has a certain amount of money stashed. All houses at this 
# place are arranged in a circle. That means the first house is the 
# neighbor of the last one. Meanwhile, adjacent houses have a security 
# system connected, and it will automatically contact the police if two 
# adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each 
# house, return the maximum amount of money you can rob tonight without 
# alerting the police.

class Solution:    
    def rob(self, nums: List[int]) -> int:
        def robber(nums, mem, n, low):            
            if n<=low:
                return mem.get(n,0)
            
            if n in mem:
                return mem[n]            
            max_prof = max(robber(nums, mem, n-2, low)+nums[n], robber(nums, mem, n-1, low))
            mem[n] = max_prof
            return max_prof  
        
        le = len(nums)
        if le==1:
            return nums[0]
        
        mem={0:nums[0]}
        withf = robber(nums, mem, le-2, 0) #houses [0:n-1]          
        mem={1:nums[1]}
        witho = robber(nums, mem, le-1, 1) #houses [1:n]
        
        return max(withf, witho)
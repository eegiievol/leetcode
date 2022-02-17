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
        def robber(mem, n, low):            
            if n<low:
                return 0
            if n==low:
                return nums[low]
            if n in mem:
                return mem[n]            
            max_prof = max(robber(mem, n-2, low)+nums[n], robber(mem, n-1, low))
            mem[n] = max_prof
            return max_prof  
        
        if len(nums)==1:
            return nums[0]
        
        return max(robber({}, len(nums)-2, 0), \
                   robber({}, len(nums)-1, 1))
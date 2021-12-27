# You are a professional robber planning to rob houses along a street. 
# Each house has a certain amount of money stashed, the only 
# constraint stopping you from robbing each of them is that adjacent 
# houses have security systems connected and it will automatically 
# contact the police if two adjacent houses were broken into on the 
# same night.

# Given an integer array nums representing the amount of money of 
# each house, return the maximum amount of money you can rob tonight 
# without alerting the police.

class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums, mem, n):            
            if n<1:
                return mem[n]  
            
            if n in mem:
                return mem[n]
        
            max_prof = max(helper(nums, mem, n-2)+nums[n], helper(nums, mem, n-1))
            mem[n] = max_prof
            return max_prof
        
        mem = {-1:0, 0:nums[0]}
        return helper(nums, mem, len(nums)-1)
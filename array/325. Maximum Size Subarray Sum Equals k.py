# Given an integer array nums and an integer k, return the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.

 

# Example 1:

# Input: nums = [1,-1,5,-2,3], k = 3
# Output: 4
# Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.


class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prefsum = []
        tmp = 0
        le=len(nums)        
            
        # 1.memorize prefix sum
        for i, val in enumerate(nums):
            tmp+=val
            prefsum.append(tmp)  
        
        # 2.finding i,j is similiar issue to 2sum problem
        # we save only first occurences of prefsum elements
        hm = {} 
        for i, val in enumerate(prefsum):          
            if val not in hm:       #we register first occurences only
                hm[val]=i 
                
        ans = 0     
        for i, val in enumerate(prefsum):
            if val == k:
                ans = max(ans, i+1)
            if val-k in hm:     
                ans = max(ans, i-hm[val-k])   
        
        return ans
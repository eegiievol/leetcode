# Given an array of positive integers nums and a positive integer target, 
# return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] 
# of which the sum is greater than or equal to target. If there is no such subarray, 
# return 0 instead. 

# Example 1:
# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:        
        le = len(nums)        
        ans = float('inf')  
        l=0
        summ=0
        for r in range(le): 
            summ += nums[r]
            while l<=r and summ>=target:
                ans = min(ans, r-l+1)
                summ-=nums[l]
                l+=1
        return ans if ans != float('inf') else 0      
      

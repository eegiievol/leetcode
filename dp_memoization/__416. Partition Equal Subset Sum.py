'''
Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

 

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
'''
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        @lru_cache(maxsize=None)
        def dp(i, total):
            if total == 0:
                return True
            if i==0 or total<0:
                return False
            if dp(i-1, total) or dp(i-1, total-nums[i]):
                return True
        
        summ = sum(nums)
        if summ % 2:
            return False
        
        return dp(len(nums)-1, summ//2)
        

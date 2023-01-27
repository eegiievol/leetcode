# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# A subarray is a contiguous part of an array.

 

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

class Solution:
    #Dynamic Programming, Kadane's Algorithm
    def maxSubArray(self, nums: List[int]) -> int:
        curr, maxx = nums[0],nums[0]
        
        for num in nums[1:]:
            curr = max(num, curr + num)
            maxx = max(maxx, curr)
        
        return maxx
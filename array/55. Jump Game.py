# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.

 

# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        canreach = nums[0] #farest index we can reach 
        le=len(nums)
        
        i=1
        dest = 0
        while i<le:
            if canreach>=le-1:
                return True
            dest = canreach                       
            while i<=dest:                
                if nums[i]+i>canreach:
                    canreach = nums[i]+i  
                i+=1             
            i=dest #fix to exact position            
            if canreach==dest:
                return False           
        
        return True

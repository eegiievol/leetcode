# You are given two integer arrays nums and multipliers of size n and m 
# respectively, where n >= m. The arrays are 1-indexed.

# You begin with a score of 0. You want to perform exactly m operations. 
# On the ith operation (1-indexed), you will:

# Choose one integer x from either the start or the end of the array nums.
# Add multipliers[i] * x to your score.
# Remove x from the array nums.
# Return the maximum score after performing m operations.

class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:        
        
        def dp(m, i, j):
            mu=multipliers[m]            
            if (i,j) in mem:
                return mem[(i,j)]
                
            if m==mulen:                
                return max(nums[i]*mu, nums[j]*mu)
            
            if i==j:
                return nums[i]*mu
            
            maxx = max(dp(m+1, i+1, j)+nums[i]*mu, dp(m+1, i, j-1)+nums[j]*mu)
            mem[(i,j)] = maxx
            return maxx
        
        mem = {}
        mulen=len(multipliers)-1
        arrlen=len(nums)-1
        return dp(0, 0, arrlen)
        
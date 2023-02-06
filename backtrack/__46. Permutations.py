class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(k, nums):
            if k==len(nums):
                ans.append(nums[:])
            
            for i in range(k, len(nums)):
                nums[k], nums[i] = nums[i], nums[k]
                backtrack(k+1, nums)
                nums[k], nums[i] = nums[i], nums[k]                
        
        ans = []
        backtrack(0, nums)
        return ans


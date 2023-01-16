class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        le=len(nums)
        if le<2:
            return nums
        arr = [1]*le      
        
        multiplier=1       
        for i in range(0,le):
            arr[i]=multiplier
            multiplier*=nums[i]

        multiplier=1
        for i in range(le-1,-1,-1):
            arr[i] *= multiplier
            multiplier*=nums[i]
        
        return arr
        
            
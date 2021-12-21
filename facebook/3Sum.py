class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        le=len(nums)
        dct = {}   
        ans=[]
    
        for i in range(le):
            su = -nums[i]
            dct = {}
            for j in range(i+1,le):
                
                if i==j:
                    continue
                if su-nums[j] in dct:
                    sub = sorted([nums[i], nums[j], su-nums[j]])
                    if sub not in ans:
                        ans.append(sub)
                dct[nums[j]]=1    
        
        return ans
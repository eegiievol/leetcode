class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        ctr = {}
        for el in nums:            
            if el not in ctr:
                ctr[el] = 1
            else:
                ctr[el]+=1                
        
        for it,v in ctr.items():
            if v>1:
                ans.append(it)
        return ans
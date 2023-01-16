# Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

 

# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pref = []
        tmp = 0
        ans=0
        
        for num in nums:    #prepare prefix sum first
            tmp+=num
            pref.append(tmp)        
        
        #rest of the task is just '2SUM problem' actually, 
        #but we need count all possible combinations
        prmap = defaultdict(list)
        for i,val in enumerate(pref):
            if val-k in prmap: 
                ans+=len(prmap[val-k]) #count matches found so far                      
            prmap[val].append(i)            
            if val==k:  #special case
                ans+=1
               
        print(prmap)
                
        return ans

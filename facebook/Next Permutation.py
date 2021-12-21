# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

# If such an arrangement is impossible, it must rearrange it to the lowest possible order (i.e., sorted in ascending order).

# The replacement must be in place and use only constant extra memory.


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:  
        def findNextNum(arr,leng,i):
            j=leng-1
            while j>i:
                if arr[j]>arr[i]:
                    return j
                j-=1
        
        le=len(nums)        
        i=le-2        
        
        #find first decreasing number
        while i>=0: 
            if nums[i]<nums[i+1]:
                break
            i-=1
        
        #no next perm
        if i==-1:
            nums[::]=nums[::-1]
            return      
        
            
        #swap with next higher element to the right
        nxt=findNextNum(nums,le,i)
        nums[i],nums[nxt]=nums[nxt],nums[i]
        #print(nums)
    
        #reverse [i+1:]
        nums[::] = nums[:i+1]+sorted(nums[i+1:])
          

        
    
    
        
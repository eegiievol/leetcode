# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, 
# representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
# To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that 
# should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:        
        
        if n==0:
            return
        if m==0:
            nums1[::] = nums2[::]
        
        ptr = m+n-1        
        i,j=m-1,n-1
        while ptr>=0:
            if i<0:
                nums1[:j+1] = nums2[:j+1]
                return
            elif j<0:
                return
            
            if nums1[i]>nums2[j]:
                nums1[ptr] = nums1[i]
                i-=1
            else:
                nums1[ptr] = nums2[j]            
                j-=1
            ptr-=1
        
                
        


 
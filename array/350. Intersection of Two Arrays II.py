# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

 

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]


#EEGII: THIS PROBLEM IS NOT INTERSECTION AT ALL, IT JUST RETURNING COMMON ELEMENTS IN 2 ARRAYS
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1)>len(nums2):
            return self.intersect(nums2, nums1)        

        m = Counter(nums1)        
        k=0

        for num in nums2:
            if m[num]>0:
                m[num]-=1
                nums1[k]=num
                k+=1
        
        return nums1[:k:]
        
        
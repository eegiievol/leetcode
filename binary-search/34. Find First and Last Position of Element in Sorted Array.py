# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l,r = 0, len(nums)-1
        first,second = -1, -1
        
        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target and (mid==0 or nums[mid-1]!=target):
                first = mid
                break
            if nums[mid]>=target:
                r=mid-1
            elif nums[mid]<target:
                l=mid+1
        
        l,r = 0, len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target and (mid==len(nums)-1 or nums[mid+1]!=target):
                second = mid
                break
            if nums[mid]>target:
                r=mid-1
            elif nums[mid]<=target:
                l=mid+1
            
        
        return [first, second]
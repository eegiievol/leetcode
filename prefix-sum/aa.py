'''
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

 

Example 1:

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
Example 2:

Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
'''

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        #nums             0 1 1 [0 1 0 1 0 1] 
        #prefix_sum      -1 0 1  0 1 0 1 0 1
        #matching             1            1      (prefix_sum[i]==prefix_sum[j] where i is the earliest)

        prefix_sum = [0 for _ in range(len(nums))]
        occurences = {0:-1}

        ones = 0
        for i, num in enumerate(nums):
            if num > 0: ones += 1
            else: ones -= 1
            prefix_sum[i] = ones
            
            #record unique occurences
            if ones not in occurences:
                occurences[ones] = i
        
        #reverse loop and find match
        ans = -1
        for j in range(len(prefix_sum)-1, -1, -1):
            if prefix_sum[j] in occurences:
                ans = max(ans, j - occurences[prefix_sum[j]])

        return ans
    
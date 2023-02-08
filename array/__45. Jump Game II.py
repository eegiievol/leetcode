'''
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2
 
'''
class Solution:
    def jump(self, nums: List[int]) -> int:
        can_reach = 0
        max_reach = 0
        steps = 0
        for i in range(len(nums)-1):
            max_reach = max(max_reach, i+nums[i])

            if can_reach == i:
                can_reach = max_reach
                steps += 1
        
        return steps
'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        cur, res = 0, 0

        # monotonic stack
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                tmp = stack.pop()
                if not stack:
                    break
                distance = i - stack[-1] - 1
                res += distance * (min(height[i], height[stack[-1]]) - height[tmp])

            # keep monotonic pace
            stack.append(i)
        return res
        

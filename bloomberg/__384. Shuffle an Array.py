'''
Given an integer array arr and a target value target, return the integer value such that when we change all the integers larger than value in the given array to be equal to value, the sum of the array gets as close as possible (in absolute difference) to target.

In case of a tie, return the minimum such integer.

Notice that the answer is not neccesarilly a number from arr.

 

Example 1:

Input: arr = [4,9,3], target = 10
Output: 3
Explanation: When using 3 arr converts to [3, 3, 3] which sums 9 and that's the optimal answer.
Example 2:

Input: arr = [2,3,5], target = 10
Output: 5
Example 3:

Input: arr = [60864,25176,27249,21296,20204], target = 56803
Output: 11361
 
'''

import random

class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums[:]
        self.shuffled = nums[:]
        

    def reset(self) -> List[int]:
        return self.original

    def shuffle(self) -> List[int]:
        n = len(self.shuffled)
        for i in range(n):
            swap_index = random.randrange(0, n)
            self.shuffled[i], self.shuffled[swap_index] = self.shuffled[swap_index], self.shuffled[i]
        return self.shuffled


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

'''
You are given an array nums of n positive integers.

You can perform two types of operations on any element of the array any number of times:

If the element is even, divide it by 2.
For example, if the array is [1,2,3,4], then you can do this operation on the last element, and the array will be [1,2,3,2].
If the element is odd, multiply it by 2.
For example, if the array is [1,2,3,4], then you can do this operation on the first element, and the array will be [2,2,3,4].
The deviation of the array is the maximum difference between any two elements in the array.

Return the minimum deviation the array can have after performing some number of operations.

 

Example 1:

Input: nums = [1,2,3,4]
Output: 1
Explanation: You can transform the array to [1,2,3,2], then to [2,2,3,2], then the deviation will be 3 - 2 = 1.
Example 2:

Input: nums = [4,1,5,20,3]
Output: 3
Explanation: You can transform the array after two operations to [4,2,5,5,3], then the deviation will be 5 - 2 = 3.
Example 3:

Input: nums = [2,10,8]
Output: 3
'''
import heapq

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:

        evens = []
        for num in nums:
            if num % 2:
                evens.append(-num*2)
            else:
                evens.append(-num)
        
        minimum = -max(evens)
        heapq.heapify(evens)

        min_deviation = float('inf')
        while evens:
            cur = -heapq.heappop(evens)
            min_deviation = min(min_deviation, cur-minimum)

            if cur%2==0:
                heapq.heappush(evens, -cur//2)
                minimum = min(minimum, cur//2)
            else:
                break

        return min_deviation

'''
By transforming all odd numbers to even numbers, we can always divide even numbers by 2, so the maximum value in the array can be reduced to its minimum possible value. We also keep track of the minimum value in the array, since we can only increase it by multiplying it by 2.

We then repeatedly pop the maximum value from the priority queue, which guarantees that we are always reducing the maximum value in the array. If the maximum value is odd, we can no longer divide it by 2, so we break out of the loop. Otherwise, we divide the maximum value by 2, which reduces the maximum value, and update the minimum value accordingly.
'''
        


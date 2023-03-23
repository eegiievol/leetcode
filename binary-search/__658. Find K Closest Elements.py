'''
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. 
The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
 

Example 1:
Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]

Example 2:
Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]
'''

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if len(arr) == k:
            return arr
        
        left = bisect_left(arr, x) - 1
        right = left + 1

        while right - left + 1 < k + 2: #if length is shorter than k+2
            if left == -1:
                right += 1
                continue
            
            if right == len(arr):
                left -=1
                continue
            
            #Whichever pointer has the closer number, move that pointer towards the edge to include that element in our output.
            if abs(arr[left] - x) <= abs(arr[right] - x):
                left -= 1
            else:
                right += 1
        
        #return 'left+1' to 'right-1'
        return arr[left + 1:right]

'''
Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

You must find a solution with a memory complexity better than O(n2).

 

Example 1:

Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
Example 2:

Input: matrix = [[-5]], k = 1
Output: -5
'''
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        #heapify
        heap = []
        rowlen, collen = len(matrix), len(matrix[0])
        for i in range(rowlen):
            heappush(heap, (matrix[i][0], i))
        
        #column pointers
        ptrs = [0 for i in range(rowlen)]

        #pop heap k times while incrementing col pointers in a same row
        for _ in range(k):
            popped, row = heappop(heap)
            if ptrs[row]<rowlen-1:
                col = ptrs[row]
                heappush(heap, (matrix[row][col+1], row))
                ptrs[row] += 1
        
        return popped

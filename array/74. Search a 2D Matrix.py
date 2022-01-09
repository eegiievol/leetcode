# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowsize,colsize = len(matrix), len(matrix[0])
        l,r = 0, rowsize*colsize-1
        
        while l<=r:
            mid = (l+r)//2            
            mrow, mcol = mid//colsize, mid%colsize
            
            if matrix[mrow][mcol]==target:
                return True
            if matrix[mrow][mcol]>target:
                r=mid-1
            elif matrix[mrow][mcol]<target:
                l=mid+1
        
        return False

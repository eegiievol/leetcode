# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

# Example 1:

# Input: rowIndex = 3
# Output: [1,3,3,1]

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        @cache
        def getNumber(row, col):
            if row==0 and col==0:
                return 1
            if col<0 or col>row:
                return 0        
            return getNumber(row-1, col-1)+getNumber(row-1, col)
        
        ans = []
        
        for i in range(rowIndex+1):
            ans.append(getNumber(rowIndex, i))
            
        return ans

# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
# The robot can only move either down or right at any point in time. The robot is trying to reach 
# the bottom-right corner of the grid (marked 'Finish' in the diagram below).
# Now consider if some obstacles are added to the grids. How many unique paths would there be?
# An obstacle and space is marked as 1 and 0 respectively in the grid.

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:        
        def helper(coord, rs, cs):
            row, col = coord
            if row<0 or row>=rs or col<0 or col>=cs: #out of range             
                return 0            
            if obstacleGrid[row][col]==1:
                return 0            
            if row==rs-1 and col==cs-1:
                return 1 
            if coord in mat:
                return mat[coord]
        
            summ = helper((row, col+1), rs, cs) + helper((row+1, col), rs, cs)
            mat[coord] = summ
            return summ        
        
        mat = {}
        return helper((0,0), len(obstacleGrid), len(obstacleGrid[0]))

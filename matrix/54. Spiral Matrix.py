'''
Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

'''

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        height, width = len(matrix), len(matrix[0])
        ans = []
        visited = 0
        for i in range(width):
            for col in range(i, width-i):
                ans.append(matrix[i][col])
                visited += 1
                if visited==width*height:
                    return ans
            for row in range(i+1, height-i): 
                ans.append(matrix[row][width-i-1])
                visited += 1
                if visited==width*height:
                    return ans
            for col in range(width-i-2, i-1, -1):
                ans.append(matrix[height-i-1][col])
                visited += 1
                if visited==width*height:
                    return ans
            for row in range(height-i-2, i, -1):                
                ans.append(matrix[row][i])
                visited += 1
                if visited==width*height:
                    return ans

        return ans
                    
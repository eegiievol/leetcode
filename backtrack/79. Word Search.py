# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

# Example 1:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def backtrack(visited, index, coordinate):
            row, col = coordinate
            visited[row][col] = 1
            if index==len(word)-1:
                return True

            for r,c in [(1,0),(0,1),(-1,0),(0,-1)]:
                newrow, newcol = row+r, col+c
                if 0<=newrow<height and 0<=newcol<width and \
                        board[newrow][newcol]==word[index+1] and not visited[newrow][newcol]:
                    if backtrack(visited, index+1, (newrow, newcol)):
                        return True
            visited[row][col] = 0
            return False

        height, width = len(board), len(board[0]) 
        visited = [[0]*width for i in range(height)]

        for i in range(height):
            for j in range(width):
                if board[i][j]==word[0] and backtrack(visited, 0, (i,j)):
                    return True
        return False

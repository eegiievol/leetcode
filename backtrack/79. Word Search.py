# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

# Example 1:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(r,c,i):
            visited[r][c]=True
            if i==len(word)-1 and board[r][c]==word[len(word)-1]:
                return True
            directions = [(0,1),(1,0),(-1,0),(0,-1)]
            for ro, co in directions:
                if 0<=r+ro<len(board) and 0<=c+co<len(board[0]) and board[r+ro][c+co]==word[i+1] and not visited[r+ro][c+co]:
                    if backtrack(r+ro, c+co, i+1):
                        return True
            visited[r][c]=False        
            return False
    
        
        visited = [[False]*len(board[0]) for _ in range(len(board))]
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col]==word[0]:
                    if backtrack(row,col,0):
                        return True
        return False

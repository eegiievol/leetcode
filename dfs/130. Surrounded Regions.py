# Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

# A region is captured by flipping all 'O's into 'X's in that surrounded region.

 

# Example 1:


# Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
# Explanation: Surrounded regions should not be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(r,c):
            if r<0 or r>=maxr:
                return
            if c<0 or c>=maxc:
                return
            directions = [(0,1), (1,0), (-1,0), (0,-1)]
            if board[r][c]=='O':
                board[r][c]='V'
                for ro,co in directions:
                    dfs(r+ro,c+co)
        
        maxr,maxc = len(board), len(board[0])
        for i in range(maxc):
            dfs(0, i)
            dfs(maxr-1,i)
        for i in range(maxr):
            dfs(i,0)
            dfs(i,maxc-1)
        
        for r in range(maxr):
            for c in range(maxc):
                if board[r][c]=='O':
                    board[r][c]='X'
                elif board[r][c]=='V':
                    board[r][c]='O'

# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(list)
        col = defaultdict(list)
        box = defaultdict(list)
        
        #verify rows
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c]=='.':
                    continue
                
                #verify rows
                if board[r][c] in row[r]:
                    return False
                #verify cols
                if board[r][c] in col[c]:
                    return False
                
                #verify boxes
                boxnum = (r//3)*3+c//3
                if board[r][c] in box[boxnum]:
                    return False
                
                box[boxnum].append(board[r][c])
                col[c].append(board[r][c])
                row[r].append(board[r][c])
        
        return True

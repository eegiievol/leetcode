'''
You are starving and you want to eat food as quickly as possible. You want to find the shortest path to arrive at any food cell.

You are given an m x n character matrix, grid, of these different types of cells:

'*' is your location. There is exactly one '*' cell.
'#' is a food cell. There may be multiple food cells.
'O' is free space, and you can travel through these cells.
'X' is an obstacle, and you cannot travel through these cells.
You can travel to any adjacent cell north, east, south, or west of your current location if there is not an obstacle.

Return the length of the shortest path for you to reach any food cell. If there is no path for you to reach food, return -1.
 

Example 1:
Input: grid = [["X","X","X","X","X","X"],
               ["X","*","O","O","O","X"],
               ["X","O","O","#","O","X"],
               ["X","X","X","X","X","X"]]
Output: 3
Explanation: It takes 3 steps to reach the food.
Example 2:

Input: grid = [["X","X","X","X","X"],
               ["X","*","X","O","X"],
               ["X","O","X","#","X"],
               ["X","X","X","X","X"]]
Output: -1
Explanation: It is not possible to reach the food.
Example 3:


Input: grid = [["X","X","X","X","X","X","X","X"],
               ["X","*","O","X","O","#","O","X"],
               ["X","O","O","X","O","O","X","X"],
               ["X","O","O","O","O","#","O","X"],
               ["X","X","X","X","X","X","X","X"]]
Output: 6
Explanation: There can be multiple food cells. It only takes 6 steps to reach the bottom food.

'''
class Solution:
    def getFood(self, grid: List[List[str]]) -> int:

        steps = 0
        q = deque()

        m, n = len(grid), len(grid[0])
        [q.append((i,j)) for j in range(n) for i in range(m) if grid[i][j]=='*']

        while q:
            steps += 1
            for _ in range(len(q)):
                ro, co = q.popleft()
                for r, c in [(0,1), (1,0), (-1,0), (0,-1)]:
                    newrow, newcol = r+ro, c+co
                    if 0<=newrow<m and 0<=newcol<n:
                        if grid[newrow][newcol] == 'O':
                            q.append((newrow, newcol))
                            grid[newrow][newcol] = 'X'
                        elif grid[newrow][newcol] == '#':
                            return steps

        return -1

# 1. Simulation, please notice that you need to confirm grid value is 2 rather than using else because it might be 0.
# 2. Try to make the code as short as possible in the future.
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        grid = [[0 for j in range(3)] for i in range(3)]
        n = len(moves)
        for i in range(n):
            x, y = moves[i]
            if i % 2 == 0:
                grid[x][y] = 1
            else:
                grid[x][y] = 2
        for i in range(3):
            if grid[i][0] == grid[i][1] and grid[i][0] == grid[i][2]:
                if grid[i][0] == 1:
                    return 'A'
                elif grid[i][0] == 2:
                    return 'B'
        for j in range(3):
            if grid[0][j] == grid[1][j] and grid[0][j] == grid[2][j]:
                if grid[0][j] == 1:
                    return 'A'
                elif grid[0][j] == 2:
                    return 'B'
        if grid[0][0] == grid[1][1] and grid[0][0] == grid[2][2]:
            if grid[0][0] == 1:
                return 'A'
            elif grid[0][0] == 2:
                return 'B'
        if grid[0][2] == grid[1][1] and grid[2][0] == grid[0][2]:
            if grid[0][2] == 1:
                return 'A'
            elif grid[0][2] == 2:
                return 'B'
        if n < 9:
            return 'Pending'
        else:
            return 'Draw'
                
                
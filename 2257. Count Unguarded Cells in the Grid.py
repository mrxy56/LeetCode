class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        directions = ((0, 1), (0, -1), (-1, 0), (1, 0))
        grid = [[0 for j in range(n)] for i in range(m)] # Use space in exchange of time
        mp = {'U': 0, 'D': 1, 'L': 2, 'R': 3}
        self.cnt = 0
        def isvalid(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            return True
        
        def dfs(i, j, direction):
            if grid[i][j] == 1 or grid[i][j] == 2: # An optimization, if meet 'G', stop
                return
            if grid[i][j] == 0:
                grid[i][j] = -1
                self.cnt += 1
            d = directions[mp[direction]]
            ni = i + d[0]
            nj = j + d[1]
            if isvalid(ni, nj):
                dfs(ni, nj, direction)
        
        for wall in walls:
            x, y = wall
            grid[x][y] = 1
        for guard in guards:
            x, y = guard
            grid[x][y] = 2
        for guard in guards:
            i, j = guard
            for dirc in ['U', 'D', 'L', 'R']:
                d = directions[mp[dirc]]
                if isvalid(i + d[0], j + d[1]): # must make sure the next grid is valid
                    dfs(i + d[0], j + d[1], dirc)
        return m * n - self.cnt - len(walls) - len(guards)
                
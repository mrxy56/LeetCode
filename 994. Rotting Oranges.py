class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        d = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        r, c = len(grid), len(grid[0])
        q = []
        ans = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
        def valid(x, y):
            if x >= 0 and x < r and y >= 0 and y < c:
                return True
            return False
        while(q):
            x, y, day = q.pop(0)
            if day > ans:
                ans = day
            for dd in d:
                nx = x + dd[0]
                ny = y + dd[1]
                if valid(nx, ny):
                    if grid[nx][ny] == 1:
                        q.append((nx, ny, day + 1))
                        grid[nx][ny] = 2
                    
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    return -1
        return ans
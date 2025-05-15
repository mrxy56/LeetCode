class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        vis = set()
        n = len(grid)
        if grid[0][0] == 1:
            return -1
        q = [(0, 0, 0)]
        vis.add((0, 0))
        d = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        while q:
            x, y, dis = q.pop(0)
            if x == n - 1 and y == n - 1:
                return dis + 1
            for dd in d:
                nx = x + dd[0]
                ny = y + dd[1]
                if nx >= 0 and nx < n and ny >= 0 and ny < n and grid[nx][ny] == 0 and (nx, ny) not in vis:
                    q.append((nx, ny, dis + 1))
                    vis.add((nx, ny))
        return -1
                
        
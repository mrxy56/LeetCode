class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def isvalid(a, b):
            if a >= 0 and a < len(grid) and b >= 0 and b < len(grid[0]):
                return True
            return False
        visited = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]
        q = []
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and not visited[i][j]:
                    q.append((i, j))
                    visited[i][j] = 1
                    cnt = 0
                    while(q):
                        x, y = q.pop(0)
                        cnt += 1
                        for a, b in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                            if isvalid(a, b) and grid[a][b] == 1 and not visited[a][b]:
                                q.append((a, b))
                                visited[a][b] = 1
                    if cnt > ans:
                        ans = cnt
        return ans
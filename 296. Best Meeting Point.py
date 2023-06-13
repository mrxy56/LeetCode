class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        xs = [0 for i in range(m)]
        ys = [0 for i in range(n)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    xs[i] += 1
                    ys[j] += 1
        dis = m * m * n * n
        for i in range(m):
            for j in range(n):
                tmp = 0
                for k in range(m):
                    tmp += xs[k] * abs(k - i)
                for t in range(n):
                    tmp += ys[t] * abs(t - j)
                if tmp < dis:
                    dis = tmp
        return dis
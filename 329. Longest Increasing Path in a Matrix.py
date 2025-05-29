class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        mp = {}
        ans = 0
        @lru_cache(None)
        def dfs(x, y):
            tmp = 0
            flag = False
            for d in direction:
                nx = x + d[0]
                ny = y + d[1]
                if nx >= 0 and nx < n and ny >= 0 and ny < m and matrix[nx][ny] > matrix[x][y]:
                    tmp = max(tmp, dfs(nx, ny))
                    flag = True
            if not flag:
                return 1
            return tmp + 1
        for i in range(n):
            for j in range(m):
                ans = max(ans, dfs(i, j))
        return ans
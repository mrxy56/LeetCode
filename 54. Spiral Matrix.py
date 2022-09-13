class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        m, n = len(matrix), len(matrix[0])
        def dfs(x, y, mode):
            if x < 0 or x >= m or y < 0 or y >= n or matrix[x][y] == -200:
                return
            ans.append(matrix[x][y])
            matrix[x][y] = -200
            if mode == 'u':
                dfs(x - 1, y, 'u')
            dfs(x, y + 1, 'r')
            dfs(x + 1, y, 'd')
            dfs(x, y - 1, 'l')
            dfs(x - 1, y, 'u')
        dfs(0, 0, 'r')
        return ans
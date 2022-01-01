# Remember else dp[i][j] = 0 if matrix[i - 1][j - 1] == '0'.
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        if rows:
            cols = len(matrix[0])
        else:
            cols = 0
        maxnum = 0
        dp = [[0 for j in range(cols + 1)] for i in range(rows + 1)]
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                if matrix[i - 1][j - 1] == '1':
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1
                    if dp[i][j] > maxnum:
                        maxnum = dp[i][j]
                else:
                    dp[i][j] = 0
        return maxnum * maxnum
        
# 1. The index is very tricky.
# 2. We need to calculate the minimum rather than the maximum.
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[0 for j in range(n)] for i in range(n)]
        dp[0][0] = triangle[0][0]
        for i in range(1, n):
            for j in range(i + 1):
                if j > 0 and j < i:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] + triangle[i][j]
                elif j == i:
                    dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
        ans = 2 << 31 - 1
        for j in range(n):
            ans = min(ans, dp[n - 1][j])
        return ans
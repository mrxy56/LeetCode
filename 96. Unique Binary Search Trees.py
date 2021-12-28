# Interval DP, easy to make mistakes when choosing i, and rememter the numbers of left and right need to be multiplied rather than added.
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [[0 for i in range(n + 1)] for j in range(n + 1)]
        for i in range(1, n + 1):
            dp[i][i] = 1
        for L in range(2, n + 1):
            for i in range(1, n - L + 2):
                j = min(i + L - 1, n)
                for k in range(i, j + 1):
                    if k - 1 >= i and k + 1 < j + 1:
                        dp[i][j] += dp[i][k - 1] * dp[k + 1][j]
                    elif k - 1 >= i:
                        dp[i][j] += dp[i][k - 1]
                    elif k + 1 < j + 1:
                        dp[i][j] += dp[k + 1][j]
        return dp[1][n]
                
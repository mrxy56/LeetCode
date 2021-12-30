# CompletePack, no need to iterate number of items, just do not set limitations for item choosing.
class Solution:
    def numSquares(self, n: int) -> int:
        sqrnums = []
        for i in range(1, 101):
            sqrnums.append(i * i)
        dp = [10000 for i in range(n + 1)]
        dp[0] = 0
        m = len(sqrnums)
        for v in range(1, n + 1):
            for i in range(m):
                if v < sqrnums[i]:
                    break
                dp[v] = min(dp[v - sqrnums[i]] + 1, dp[v])
        return dp[n]
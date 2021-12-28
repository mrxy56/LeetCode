# It is pretty difficult to tell the difference between 0-based when indexing strings and 1-based when infering dps.
# And the initialization is really interesting too, dp[i][j] means whether there is anyway to form an i + j length string using i s1 and j s2 characters.
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if not ((m + n) == len(s3)):
            return False
        dp = [[0 for j in range(n + 1)] for i in range(m + 1)]
        dp[0][0] = 1
        for i in range(1, m + 1):
            if s1[i - 1] == s3[i - 1]:
                dp[i][0] = dp[i - 1][0]
        for j in range(1, n + 1):
            if s2[j - 1] == s3[j - 1]:
                dp[0][j] = dp[0][j - 1]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s3[i + j - 1] == s1[i - 1]:
                    dp[i][j] = dp[i][j] or dp[i - 1][j]
                if s3[i + j - 1] == s2[j - 1]:
                    dp[i][j] = dp[i][j] or dp[i][j - 1]
        return dp[m][n]
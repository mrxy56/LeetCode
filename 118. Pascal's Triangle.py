# imagine it is a rectangle triangle.
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        n = numRows
        dp = [[0 for j in range(n)] for i in range(n)]
        ans = []
        for i in range(n):
            dp[i][0] = 1
            dp[i][i] = 1
        for i in range(2, n):
            for j in range(1, n - 1):
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
        for i in range(n):
            tmp = []
            for j in range(i + 1):
                tmp.append(dp[i][j])
            ans.append(tmp)
        return ans
            
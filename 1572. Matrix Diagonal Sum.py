# 1. Odd and Even are different.
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans = 0
        n = len(mat)
        for i in range(n):
            ans += mat[i][i]
        for i in range(n):
            ans += mat[i][n - 1 - i]
        if n % 2 == 1:
            ans -= mat[n // 2][n // 2]
        return ans
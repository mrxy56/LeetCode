# 1. Another way is to fold through diagonal and flip according to the mid line.
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        r = n
        c = m
        if n % 2 == 0:
            r = n // 2
            c = m // 2
        if n % 2 == 1:
            r = n // 2 + 1
            c = m // 2
        for i in range(r):
            for j in range(c):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
                matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
                matrix[j][n - 1 - i] = tmp
        return matrix
        
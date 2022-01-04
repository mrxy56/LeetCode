# Another way is to calculate 0 rows and columns.
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    for k in range(n):
                        if matrix[i][k]!=0:
                            matrix[i][k] = None
                    for k in range(m):
                        if matrix[k][j]!=0:
                            matrix[k][j] = None
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == None:
                    matrix[i][j] = 0
        return matrix
# Otherwise, print the original matrix.
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        a = [[0 for j in range(c)] for i in range(r)]
        m, n = len(mat), len(mat[0])
        if m * n != r * c:
            return mat
        tmp = []
        for i in range(m):
            for j in range(n):
                tmp.append(mat[i][j])
        t = 0
        flag = False
        for i in range(r):
            for j in range(c):
                a[i][j] = tmp[t]
                t += 1
        return a
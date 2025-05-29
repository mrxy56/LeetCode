class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m, k = len(mat1), len(mat1[0])
        k, n = len(mat2), len(mat2[0])
        mat = [[0 for j in range(n)] for i in range(m)]
        row = {}
        col = {}
        for i in range(m):
            for j in range(k):
                if mat1[i][j] != 0:
                    if i in row:
                        row[i].append((j, mat1[i][j]))
                    else:
                        row[i] = [(j, mat1[i][j])]
                        
        for i in range(k):
            for j in range(n):
                if mat2[i][j] != 0:
                    if j in col:
                        col[j].append((i, mat2[i][j]))
                    else:
                        col[j] = [(i, mat2[i][j])]
                              
        for k1, v1 in row.items():
            for k2, v2 in col.items():
                tmp = 0
                for t1 in v1:
                    for t2 in v2:
                        if t1[0] == t2[0]:
                            tmp += t1[1] * t2[1]
                mat[k1][k2] = tmp
                
        return mat
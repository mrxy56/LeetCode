# 1. Contral limitation, contral moves.
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # (0, 0)
        # (0, 1), (1, 0)
        # (2, 0), (1, 1), (0, 2)
        # (1, 2), (2, 1)
        # (2, 2)
        
        m = len(mat)
        n = len(mat[0])
        ans = []
        
        if m == 1 or n == 1:
            for i in range(m):
                for j in range(n):
                    ans.append(mat[i][j])
            return ans
        
        flag = True
        
        for i in range(m):
            tmp = []
            x = i
            y = 0
            while x >= 0 and x < m and y >= 0 and y < n:
                tmp.append(mat[x][y])
                x -= 1
                y += 1
            if flag:
                ans = ans + tmp
                flag = False
            else:
                ans = ans + tmp[::-1]
                flag = True
        
        for j in range(1, n):
            tmp = []
            x = m - 1
            y = j
            while x >= 0 and x < m and y >= 0 and y < n:
                tmp.append(mat[x][y])
                x -= 1
                y += 1
            if flag:
                ans = ans + tmp
                flag = False
            else:
                ans = ans + tmp[::-1]
                flag = True
                
        return ans
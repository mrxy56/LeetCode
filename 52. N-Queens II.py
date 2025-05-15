# 1. For the diagnal, it has 2 * n possible values.
class Solution:
    def totalNQueens(self, n: int) -> int:
        self.ans = 0
        col = [0 for i in range(n)]
        diag1 = [0 for i in range(2 * n)]
        diag2 = [0 for i in range(2 * n)]
        def is_taken(x, y):
            if col[y] == 0 and diag1[x - y + n] == 0 and diag2[x + y] == 0:
                return False
            return True
        
        def take(x, y):
            col[y] = 1
            diag1[x - y + n] = 1
            diag2[x + y] = 1
        
        def release(x, y):
            col[y] = 0
            diag1[x - y + n] = 0
            diag2[x + y] = 0
            
        def dfs(r, c):
            take(r, c)
            for i in range(n):
                if not is_taken(r + 1, i):
                    dfs(r + 1, i)
            if r == n - 1:
                self.ans += 1
            release(r, c)
            return
          
        for i in range(n):
            if not is_taken(0, i):
                dfs(0, i)
        return self.ans
            
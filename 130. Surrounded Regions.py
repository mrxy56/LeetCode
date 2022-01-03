# Deal with edge cases first.
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def valid(i, j):
            if i >= 0 and i < m and j >=0 and j < n:
                return True
            return False
        
        def dfs(i, j, mode):
            board[i][j] = mode
            pos = [[0, 1], [1, 0], [0, -1], [-1, 0]]
            for p in pos:
                ni = i + p[0]
                nj = j + p[1]
                if valid(ni, nj) and board[ni][nj] == 'O':
                    dfs(ni, nj ,mode)
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                    if board[i][j] == 'O':
                        dfs(i, j, 'E')
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    dfs(i, j, 'X')
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'E':
                    board[i][j] = 'O'
                
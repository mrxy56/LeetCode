class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m, n = len(board), len(board[0])
        for i in range(m):
            s = set()
            for j in range(n):
                if board[i][j] in s:
                    return False
                if board[i][j] != '.':
                    s.add(board[i][j])
        for j in range(n):
            s = set()
            for i in range(m):
                if board[i][j] in s:
                    return False
                if board[i][j] != '.':
                    s.add(board[i][j])
        for i in range(0, m, 3):
            for j in range(0, n, 3):
                s = set()
                for a in range(3):
                    for b in range(3):
                        ni = i + a
                        nj = j + b
                        if ni >= 0 and ni < m and nj >= 0 and nj < n:
                            if board[ni][nj] in s:
                                return False
                            if board[ni][nj] != '.':
                                s.add(board[ni][nj])
        return True
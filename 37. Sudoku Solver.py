# 1. Pay attention to the order of backtracking.
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = [set() for i in range(9)]
        col = [set() for i in range(9)]
        g = [[set() for j in range(3)] for i in range(3)]
        self.cnt = 0
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                num = int(board[i][j])
                X = i // 3
                Y = j // 3
                row[i].add(num)
                col[j].add(num)
                g[X][Y].add(num)
                self.cnt += 1
        
        def dfs(r, c):
            if self.cnt == 81:
                return
            if board[r][c] == '.':
                X = r // 3
                Y = c // 3
                for i in range(1, 10):
                    if i not in row[r] and i not in col[c] and i not in g[X][Y]:
                        board[r][c] = str(i)
                        row[r].add(i)
                        col[c].add(i)
                        g[X][Y].add(i)
                        self.cnt += 1
                        if c < 8:
                            dfs(r, c + 1)
                        else:
                            dfs(r + 1, 0)
                        if self.cnt == 81:
                            return
                        self.cnt -= 1
                        board[r][c] = '.'
                        row[r].remove(i)
                        col[c].remove(i)
                        g[X][Y].remove(i)
            else:
                if c < 8:
                    dfs(r, c + 1)
                else:
                    dfs(r + 1, 0)
        dfs(0, 0)
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        vis = [[0 for j in range(n)] for i in range(m)]
        flag = 0
        pos = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        def valid(x, y):
            if x >= 0 and x < m and y >= 0 and y < n:
                return True
            return False
        
        def dfs(cur, x, y, vis, target, ans):
            cur_len = len(cur)
            if cur == target:
                ans.append(cur)
                return
            if cur_len >= len(target):
                return
            for p in pos:
                nx, ny = x + p[0], y + p[1]
                if valid(nx, ny) and vis[nx][ny] == 0 and target[cur_len] == board[nx][ny]:
                    vis[nx][ny] = 1
                    dfs(cur + board[nx][ny], nx, ny, vis, target, ans)
                    vis[nx][ny] = 0
            
        for i in range(m):
            for j in range(n):
                ans = []
                vis[i][j] = 1
                dfs(board[i][j], i, j, vis, word, ans)
                vis[i][j] = 0
                if len(ans) > 0:
                    return True
        return flag
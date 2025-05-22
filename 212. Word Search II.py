class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        words = set(words)
        self.ans = set()
        n, m = len(board), len(board[0])
        vis = [[0 for j in range(m)] for i in range(n)]
        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def dfs(x, y, w):
            if len(w) > 10:
                return
            if w in words and w not in self.ans:
                self.ans.add(w)
            for dd in d:
                nx = x + dd[0]
                ny = y + dd[1]
                if nx >= 0 and nx < n and ny >= 0 and ny < m and not vis[nx][ny]:
                    vis[nx][ny] = 1
                    dfs(nx, ny, w + board[nx][ny])
                    vis[nx][ny] = 0
            return
        
        for i in range(n):
            for j in range(m):
                vis[i][j] = 1
                dfs(i, j, board[i][j])
                vis[i][j] = 0
        return list(self.ans)
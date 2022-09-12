class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0 for j in range(n)] for i in range(n)]
        def dfs(x, y, num, mode):
            if x < 0 or y < 0 or x >= n or y >= n:
                return
            if ans[x][y] > 0:
                return
            
            ans[x][y] = num
            if mode == 'u': # when up, keep up until you cannot.
                dfs(x - 1, y, num + 1, 'u')
            dfs(x, y + 1, num + 1, 'r')
            dfs(x + 1, y, num + 1, 'd')
            dfs(x, y - 1, num + 1, 'l')
            dfs(x - 1, y, num + 1, 'u')
           
        dfs(0, 0, 1,'r')
        return ans
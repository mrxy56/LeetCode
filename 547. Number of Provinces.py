class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        ans = 0
        vis = [0 for i in range(n)]
        def dfs(node):
            if not vis[node]:
                vis[node] = 1
                for i in range(n):
                    if isConnected[node][i]:
                        dfs(i)
        for i in range(n):
            if not vis[i]:
                dfs(i)
                ans += 1
        return ans
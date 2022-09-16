class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        a = [[] for i in range(n)]
        vis = [0 for i in range(n)]
        for edge in edges:
            x, y = edge
            a[x].append(y)
            a[y].append(x)
            
        def dfs(x):
            vis[x] = 1
            for y in a[x]:
                if not vis[y]:
                    dfs(y)
        dfs(0)
        for i in range(n):
            if not vis[i] or len(edges) != n - 1: # Needs to verify the edges num too
                return False
        return True
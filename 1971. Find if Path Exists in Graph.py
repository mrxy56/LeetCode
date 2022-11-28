# 1. Cannot use backtracking because it is just exhausting every path.
# 2. We want to make sure every node is visited exactly once. Do not go back because we already failed this node.
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        a = [[] for i in range(n)]
        vis = [0 for i in range(n)]
        for edge in edges:
            x, y = edge
            a[x].append(y)
            a[y].append(x)
        self.cnt = 0
        
        def dfs(x):
            vis[x] = 1
            if x == destination:
                return True
            for y in a[x]:
                if not vis[y]:
                    if dfs(y):
                        return True
            return False
        if dfs(source):
            return True
        return False
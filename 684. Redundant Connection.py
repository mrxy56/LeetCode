class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        a = [[] for i in range(n + 1)]
        edges.reverse()
        for e in edges:
            x, y = e[0], e[1]
            a[x].append(y)
            a[y].append(x)
            
        def bfs(l, r, n):
            q = []
            vis = [0 for i in range(n + 1)]
            q.append(l)
            vis[l] = 1
            while q:
                x = q.pop(0)
                if x == r:
                    return True
                for y in a[x]:
                    if not vis[y]:
                        vis[y] = 1
                        q.append(y)
    
        for e in edges:
            l, r = e[0], e[1]
            for i, y in enumerate(a[l]):
                if y == r:
                    a[l][i] = l         # delete the edge by changing it to two self-loops
            for j, x in enumerate(a[r]):
                if x == l:
                    a[r][j] = r
            
            if bfs(l, r, n):
                return e
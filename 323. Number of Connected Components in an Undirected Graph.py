class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        p = [i for i in range(n)]
        r = [0 for i in range(n)]
        
        def union(x, y):
            px = find(x)
            py = find(y)
            if px == py:
                return
            if r[px] > r[py]:
                p[py] = px
            elif r[px] < r[py]:
                p[px] = py
            else:
                p[px] = py
                r[px] += 1
            return
            
        def find(x):
            if x == p[x]:
                return x
            p[x] = find(p[x])
            return p[x]
        
        for e in edges:
            union(e[0], e[1])
        for i in range(n):
            find(i)
        ans = set()
        for x in p:
            ans.add(x)
        return len(ans)
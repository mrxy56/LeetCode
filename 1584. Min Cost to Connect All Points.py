class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        e = []
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
        
        for i in range(n):
            for j in range(i + 1, n):
                e.append((i, j, abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])))
        e.sort(key = lambda x:x[2])
        ans = 0
        cnt = 0
        for edge in e:
            p0 = find(edge[0])
            p1 = find(edge[1])
            if p0 == p1:
                continue
            else:
                union(edge[0], edge[1])
                ans += edge[2]
                cnt += 1
                if cnt == n - 1:
                    break
        return ans
        
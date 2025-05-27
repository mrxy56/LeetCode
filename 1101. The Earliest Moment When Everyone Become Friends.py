# 1. Union Find + Greedy + Sort.
class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        r = [0 for i in range(n)]
        pa = [i for i in range(n)]
        self.ans = 0
        logs.sort(key = lambda x: x[0])
        def union(x, y, t):
            px = find(x)
            py = find(y)
            if px == py:
                return
            if r[px] > r[py]:
                pa[py] = px
            elif r[px] < r[py]:
                pa[px] = py
            else:
                pa[px] = py
                r[py] += 1
            self.ans = max(self.ans, t)
            return
                
        def find(x):
            if x == pa[x]:
                return x
            pa[x] = find(pa[x])
            return pa[x]
        
        for log in logs:
            t, x, y = log
            flag = True
            union(x, y, t)
            for i in range(1, n):
                if find(i) != find(i - 1):
                    flag = False
                    break
            if flag:
                break
        for i in range(n):
            find(i)
        for i in range(1, n):
            if find(i) != find(i - 1):
                return -1
        return self.ans
        
        
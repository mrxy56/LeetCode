class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        In = [0 for i in range(n + 1)]
        a = [[] for i in range(n + 1)]
        for e in relations:
            In[e[1]] += 1
            a[e[0]].append(e[1])
        q = []
        ans = []
        for i in range(1, n + 1):
            if In[i] == 0:
                q.append((i, 1))
        while q:
            v, d = q.pop(0)
            ans.append(v)
            for nv in a[v]:
                In[nv] -= 1
                if In[nv] == 0:
                    q.append((nv, d + 1))
        return d if len(ans) == n else -1
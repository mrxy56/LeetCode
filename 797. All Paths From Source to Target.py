# 1. No need to calculate indegrees, the problem said from 0 to n - 1.
# 2. Use cur + [v] rather than cur.append(v) because you are actually using an reference.
# 3. It allows revisit.
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        s = 0
        t = n - 1
        ans = []
        def dfs(v, cur):
            if v == t:
                ans.append(cur + [v])
                return
            for j in graph[v]:
                dfs(j, cur + [v])        
        dfs(s, [])
        return ans
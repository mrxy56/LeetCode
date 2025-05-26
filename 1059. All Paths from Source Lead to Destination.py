# 1. Use lru_cache to avoid repetitave computations.
class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        a = defaultdict(list)
        vis = set()
        for e in edges:
            s, t = e
            a[s].append(t)
        @lru_cache(None)
        def dfs(cur):
            if len(a[cur]) == 0:
                return True if cur == destination else False
            for to in a[cur]:
                if to in vis:
                    return False
                vis.add(to)
                flag = dfs(to)
                if not flag:
                    return False
                vis.remove(to)
            return True
        return dfs(source)
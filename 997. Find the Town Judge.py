# Topological Sort.
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indegrees = [0 for i in range(n + 1)]
        out = [[] for i in range(n + 1)]
        for t in trust:
            ss, tt = t[1], t[0]
            indegrees[tt] +=1
            out[ss].append(tt)
        for i in range(1, n + 1):
            if indegrees[i] == 0 and len(out[i]) == n - 1:
                return i
        return -1
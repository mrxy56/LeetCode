# Topological sort.
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegrees = [0 for i in range(numCourses)]
        out = [[] for i in range(numCourses)]
        all_edges = 0
        for p in prerequisites:
            first, second = p[1], p[0]
            indegrees[second] += 1
            out[first].append(second)
            all_edges += 1
        from collections import deque
        q = deque()
        for i in range(numCourses):
            if indegrees[i] == 0:
                q.append(i)
        ans = []
        edges = 0
        while(q):
            node = q.pop()
            ans.append(node)
            for n in out[node]:
                indegrees[n] -= 1
                edges +=1
                if indegrees[n] == 0:
                    q.append(n)
        if edges == all_edges:
            return ans
        else:
            return []
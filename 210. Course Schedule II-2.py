class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        a = [[] for i in range(numCourses)]
        ind = [0 for i in range(numCourses)]
        for p in prerequisites:
            x, y = p[0], p[1]
            a[x].append(y)
            a[y].append(x)
            ind[x] += 1
        
        q = []
        for i in range(numCourses):
            if ind[i] == 0:
                q.append(i)
        ans = []
        while q:
            x = q.pop(0)
            ans.append(x)
            for y in a[x]:
                ind[y] -= 1
                if ind[y] == 0:
                    q.append(y)
        if len(ans) == numCourses:
            return ans
        else:
            return []
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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
        cnt = 0
        while q:
            x = q.pop(0)
            cnt += 1
            for y in a[x]:
                ind[y] -= 1
                if ind[y] == 0:
                    q.append(y)
        if cnt == numCourses:
            return True
        return False
        
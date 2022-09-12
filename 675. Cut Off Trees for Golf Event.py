class Solution(object):
    def cutOffTree(self, forest):
        """
        :type forest: List[List[int]]
        :rtype: int
        """
        def bfs(i, j, destx, desty):
            q = deque() # deque + bfs
            visited = set()
            q.append((i, j, 0))
            while q:
                x, y, step = q.popleft()
                if x == destx and y == desty:
                    return step
                for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if nx >= 0 and nx < m and ny >=0 and ny < n and forest[nx][ny]!= 0 and (nx, ny) not in visited:
                        q.append((nx, ny, step + 1))
                        visited.add((nx, ny))
            return -1
                
        
        m, n = len(forest), len(forest[0])
        
        heap = []
        for i in range(m):
            for j in range(n):
                if forest[i][j] > 1:
                    heapq.heappush(heap, (forest[i][j], i, j))
        
        res = 0
        i, j = 0, 0

        while heap:
            _, destx, desty = heapq.heappop(heap)
            step = bfs(i, j, destx, desty)
            # print i, j, destx, desty, step
            if step < 0:
                return -1
            res += step
            i, j = destx, desty
        return res

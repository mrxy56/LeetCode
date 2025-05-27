class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        vis = set()
        n, m = len(heights), len(heights[0])
        dis = [[2 ** 31 - 1 for i in range(m)] for j in range(n)]
        direction = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        q = [(0, 0, 0)]
        dis[0][0] = 0
        heapq.heapify(q)
        while q:
            d, x, y = heapq.heappop(q)
            vis.add((x, y))
            for dd in direction:
                nx = x + dd[0]
                ny = y + dd[1]
                if nx >= 0 and nx < n and ny >= 0 and ny < m:
                    if max(dis[x][y], abs(heights[x][y] - heights[nx][ny])) < dis[nx][ny]:
                        if (nx, ny) not in vis:
                            dis[nx][ny] = max(dis[x][y], abs(heights[x][y] - heights[nx][ny]))
                            heapq.heappush(q, (dis[nx][ny], nx, ny))
        return dis[n - 1][m - 1]
            
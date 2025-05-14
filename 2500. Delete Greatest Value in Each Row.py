class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for row in grid:
            heapq.heapify(row)
        n, m = len(grid), len(grid[0])
        ans = 0
        for j in range(m):
            tmp = 0
            for i in range(n):
                x = heapq.heappop(grid[i])
                tmp = max(tmp, x)
            ans += tmp
        return ans
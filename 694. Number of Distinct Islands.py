# 1. Hard in programming. The key is to decide an origin and map all the other indexes into it.
# 2. [[0]] is a special case meaning no islands. Edge case is tricky but might be important in the interviews.
# 3. Distinct is a hint for set.

class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        self.ans = 0
        m, n = len(grid), len(grid[0])
        vis = [[0 for j in range(n)] for i in range(m)]
        all_islands = []
        def isvalid(x, y):
            if x >= 0 and x < m and y >= 0 and y < n:
                return True
            return False

        def dfs(x, y):
            cur_island.append((x, y))
            vis[x][y] = 1
            directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
            for d in directions:
                nx = x + d[0]
                ny = y + d[1]
                if isvalid(nx, ny) and not vis[nx][ny] and grid[nx][ny] == 1:
                    dfs(nx, ny)

        for i in range(m):
            for j in range(n):
                if not vis[i][j] and grid[i][j] == 1:
                    cur_island = []
                    dfs(i, j)
                    all_islands.append(cur_island)

        n = len(all_islands)
        island_set = set()
        if n == 0:
            return 0
        origin = all_islands[0]
        o_row = 50
        o_col = 50
        for ind in origin:
            o_row = min(o_row, ind[0])
            o_col = min(o_col, ind[1])

        for i in range(n):
            tmp = []
            min_row = 50
            min_col = 50
            for ind in all_islands[i]:
                min_row = min(min_row, ind[0])
                min_col = min(min_col, ind[1])
            diff_row = min_row - o_row
            diff_col = min_col - o_col
            for ind in all_islands[i]:
                x = ind[0] - diff_row
                y = ind[1] - diff_col
                tmp.append((x, y))
            island_set.add(tuple(tmp))
        return len(island_set)
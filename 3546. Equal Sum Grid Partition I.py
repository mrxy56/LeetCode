class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        n, m = len(grid), len(grid[0])
        row = [0 for i in range(n)]
        col = [0 for j in range(m)]
        for i in range(n):
            for j in range(m):
                row[i] += grid[i][j]
                col[j] += grid[i][j]
        row_sum = [0 for i in range(n)]
        col_sum = [0 for j in range(m)]
        for i in range(n):
            if i == 0:
                row_sum[i] = row[i]
            else:
                row_sum[i] = row_sum[i - 1] + row[i]
        for j in range(m):
            if j == 0:
                col_sum[j] = col[j]
            else:
                col_sum[j] = col_sum[j - 1] + col[j]
        for i in range(1, n):
            if row_sum[i - 1] == row_sum[n - 1] - row_sum[i - 1]:
                return True
        for j in range(1, m):
            if col_sum[j - 1] == col_sum[m - 1] - col_sum[j - 1]:
                return True
        return False
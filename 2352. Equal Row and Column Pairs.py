# 1. Brute Force can be O(n^3) while if using Hash to map the list into string, searching is only O(1).
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        ans = 0
        mp = {}
        for i in range(n):
            ls = []
            for j in range(m):
                ls.append(str(grid[i][j]))
            tmp = ".".join(ls)
            if tmp not in mp:
                mp[tmp] = 1
            else:
                mp[tmp] += 1
        for j in range(m):
            ls = []
            for i in range(n):
                ls.append(str(grid[i][j]))
            tmp = ".".join(ls)
            if tmp in mp:
                ans += mp[tmp]
        return ans
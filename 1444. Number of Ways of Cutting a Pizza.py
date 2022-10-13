class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        m, n, MOD = len(pizza), len(pizza[0]), 10 ** 9 + 7
        pre = [[0] * (n + 1) for _ in range(m + 1)]
        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                pre[r][c] = pre[r + 1][c] + pre[r][c + 1] - pre[r + 1][c + 1] + (pizza[r][c] == 'A') # prefix sum to calculate apples

        @lru_cache(None) # lru_cache to simplify the code
        def dp(k, r, c):
            if pre[r][c] == 0: return 0 
            if k == 0: return 1 # edge cases
            ans = 0
            for nr in range(r + 1, m):
                if pre[r][c] - pre[nr][c] > 0: # if applicable
                    ans = (ans + dp(k - 1, nr, c)) % MOD # transfer, 3 states, cut, row, rolumn
            for nc in range(c + 1, n):
                if pre[r][c] - pre[r][nc] > 0:
                    ans = (ans + dp(k - 1, r, nc)) % MOD
            return ans
        return dp(k - 1, 0, 0)


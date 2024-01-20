# 1. Get hint about state transition from the example (n = 3), then it is easy to solve it.
class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        if n == 1:
            return 1
        f = [0 for i in range(n)]
        p = [0 for i in range(n)]
        f[0] = 1
        f[1] = 2
        p[1] = 1
        for i in range(2, n):
            f[i] = (p[i - 1] * 2 % MOD + f[i - 1] % MOD + f[i - 2] % MOD) % MOD
            p[i] = (p[i - 1] % MOD + f[i - 2] % MOD) % MOD
        return f[n - 1]
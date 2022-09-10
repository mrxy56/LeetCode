class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        module = 10 ** 9 + 7
        dp = [0 for i in range(target + 1)]
        dp[0] = 1
        for _ in range(n): 
            for i in range(target, -1, -1):
                dp[i] = 0 # You must assign it to be zero because we need to add one non-zero item
                for v in range (1, k + 1):
                    if i - v >= 0: 
                        dp[i] = (dp[i] + dp[i - v]) % module
        return dp[target]
                
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        D = [0 for i in range(n)]
        if n < d:
            return -1
        for i in range(n - 1, -1 , -1):
            if i == n - 1:
                D[i] = jobDifficulty[i]
            else:
                D[i] = max(D[i + 1], jobDifficulty[i])
        @lru_cache(None)
        def dp(i, day):
            if day == d:
                return D[i]
            max_difficulty = 0
            minnum = float('inf')
            for j in range(i, n - (d - day)):
                max_difficulty = max(max_difficulty, jobDifficulty[j])
                minnum = min(dp(j + 1, day + 1) + max_difficulty, minnum)
            return minnum
        return dp(0, 1)
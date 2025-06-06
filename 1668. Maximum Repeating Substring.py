class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        n = len(sequence)
        if len(word) > len(sequence):
            return 0
        m = len(word)
        k = 0
        dp = [0 for i in range(n)]
        for i in range(n):
            if sequence[i:i + m] == word:
                dp[i] = dp[i - m] + 1
                k = max(dp[i], k)
        return k
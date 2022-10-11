class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        ans = n
        for i in range(n):
            if i + k <= n: # must include n here.
                tmp = blocks[i: i + k].count('W') # Sliding window is not hard, it is just a window sliding.
                ans = min(ans, tmp)
        return ans
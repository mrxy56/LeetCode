class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 1
        while n >= (1 + i) * i // 2:
            i += 1
        return i - 1
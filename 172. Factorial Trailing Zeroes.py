# 1. Factorization of 2s and 5s.
class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        five = 0
        two = 0
        for i in range(2, n + 1):
            while i % 5 == 0:
                i = i // 5
                five += 1
            while i % 2 == 0:
                i = i // 2
                two += 1
        ans += min(two, five)
        return ans
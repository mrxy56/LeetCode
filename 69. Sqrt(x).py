# It is very wise to calculate some number by log.
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        left = int(e**(log(x) * 0.5))
        right = left + 1
        return left if right * right > x else right
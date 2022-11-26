class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod = 1
        s = 0
        while n:
            tmp = n % 10
            n = n // 10
            prod *= tmp
            s += tmp
        return prod - s
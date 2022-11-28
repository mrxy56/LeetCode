# 1. Pay special attention to the number starting with several zeros -- use bit operation.
# 2. To be honest, I am not sure why using * 2 caused a mistake, but bit operation seems to be very straightforward, so just remember it.
class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        ls = []
        while n:
            tmp = n % 2
            ls.append(tmp)
            n = n >> 1
        bit = 31
        for num in ls:
            ans += num << bit
            bit -= 1
        return ans
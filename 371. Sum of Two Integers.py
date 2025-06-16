class Solution:
    def getSum(self, a: int, b: int) -> int:
        max_int = 0x7FFFFFFF
        mask = 0xFFFFFFFF
        while a != 0:
            c = ((a & b) << 1) & mask # mask to make sure it does not go out of scope or else we would have TLE.
            d = (a ^ b) & mask
            a = c
            b = d
        return b if b < max_int else ~(b ^ mask) # manage overflow.
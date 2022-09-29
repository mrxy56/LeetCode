class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x, y = int(a, 2), int(b, 2)
        while y:
            ans = x ^ y # calculate answer
            carry = (x & y) << 1 # calculate carry, left shift
            x, y = ans, carry # a new round
        return bin(x)[2:] # from the third bit
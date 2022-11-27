# 1. Bit operations for extracting the numbers.
# 2. When recovering, use reverse order to iterate.
class Solution:
    def findComplement(self, num: int) -> int:
        ans = 0
        ls = []
        while num:
            tmp = num ^ 1
            tmp = tmp & 1
            num = num >> 1
            ls.append(tmp)
        for num in ls[::-1]:
            ans = ans * 2 + num
        return ans
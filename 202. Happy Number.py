class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        if n == 1: # edge case
            return True
        while n != 1:
            s.add(n)
            t = n
            ans = 0
            while t:
                ans += (t % 10) ** 2
                t = t // 10
            if ans in s:
                return False
            if ans == 1:
                return True
            n = ans
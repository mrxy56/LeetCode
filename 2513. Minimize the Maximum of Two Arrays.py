# 1. To my surprise, this is binary search.
# 2. First, we find a reasonable value, use math.lcm().
# 3. Try to find a smaller one until we cannot. Use binary search.
class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        self.divisor1 = divisor1
        self.divisor2 = divisor2
        def isGood(x):
            dontUseFirst = x // self.divisor1
            dontUseSecond = x // self.divisor2
            dontUseBoth = x // math.lcm(self.divisor1, self.divisor2)
            if x - dontUseBoth < uniqueCnt1 + uniqueCnt2:
                return False
            if x - dontUseFirst < uniqueCnt1: 
                return False
            if x - dontUseSecond < uniqueCnt2:
                return False
            return True 

        l, r = 1, 10 ** 12
        while l <= r:
            m = (l + r) // 2
            flag = isGood(m)
            if(flag):
                r = m - 1
            else:
                l = m + 1
        return l
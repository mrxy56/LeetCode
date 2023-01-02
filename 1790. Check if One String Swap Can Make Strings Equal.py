# 1. One counter example, abc and fba.
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        n = len(s1)
        mis = 0
        for i in range(n):
            if s1[i] != s2[i]:
                mis += 1
        if mis == 0 or mis == 2:
            s1 = list(s1)
            s2 = list(s2)
            s1.sort()
            s2.sort()
            return True if s1 == s2 else False
        return False
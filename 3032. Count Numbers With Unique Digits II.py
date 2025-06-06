class Solution:
    def numberCount(self, a: int, b: int) -> int:
        ans = 0
        for i in range(a, b + 1):
            s = str(i)
            S = set(s)
            if len(s) == len(S):
                ans += 1
        return ans
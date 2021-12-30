# Cannot use set since there can be same alphabets.
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ss = sorted(s)
        st = sorted(t)
        n = len(st)
        for i in range(n - 1):
            if ss[i] != st[i]:
                return st[i]
        return st[-1]
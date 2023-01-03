# 1. Sliding window, so only need one loop.
# 2. Pay attention to the index.
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        m = len(p)
        from collections import Counter
        ans = []
        mp1 = Counter(s[:m])
        mp2 = Counter(p)
        for i in range(n - m + 1):
            if i != 0:
                mp1[s[i - 1]] -= 1
                mp1[s[i + m - 1]] += 1
            if mp1 == mp2:
                ans.append(i)
        return ans
            
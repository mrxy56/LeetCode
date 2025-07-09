class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        n = len(g)
        m = len(s)
        g.sort()
        s.sort()
        i = n - 1
        j = m - 1
        ans = 0
        while j >= 0:
            while i >= 0 and s[j] < g[i]:
                i -= 1
            if i < 0:
                j = -1
                break
            ans += 1
            i -= 1
            j -= 1
        return ans
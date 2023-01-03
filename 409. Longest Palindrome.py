# Ad hoc. Pay attention to the condition that the order can be changed.
class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import defaultdict
        n = len(s)
        ans = 0
        mp = defaultdict(int)
        for i in range(n):
            mp[s[i]] += 1
        for k, v in mp.items():
            ans += (v // 2) * 2
        for k, v in mp.items():
            if v % 2 == 1:
                ans += 1
                break
        return ans
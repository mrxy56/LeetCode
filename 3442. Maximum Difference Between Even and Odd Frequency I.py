class Solution:
    def maxDifference(self, s: str) -> int:
        mp = {}
        for ch in s:
            if ch in mp:
                mp[ch] += 1
            else:
                mp[ch] = 1
        odd = 0
        even = 2 ** 31 - 1
        for k, v in mp.items():
            if v % 2 == 1:
                odd = max(odd, v)
            else:
                even = min(even, v)
        return odd - even
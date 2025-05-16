class Solution:
    def frequencySort(self, s: str) -> str:
        mp = {}
        for ch in s:
            if ch in mp:
                mp[ch] += 1
            else:
                mp[ch] = 1
        ls = sorted(mp.items(), key = lambda kv : -kv[1])
        ans = ""
        for e in ls:
            for i in range(e[1]):
                ans = ans + e[0]
        return ans
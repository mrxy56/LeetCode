class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        n = len(s)
        mp = {}
        ans = 0
        i, j = -1, -1
        while i < n - 1 and j < n - 1:
            j += 1
            if j - i > 3:
                i += 1
                mp[s[i]] -= 1
            if s[j] in mp:
                mp[s[j]] += 1
            else:
                mp[s[j]] = 1
            if mp[s[j]] > 1:
                while mp[s[j]] > 1:
                    i += 1
                    mp[s[i]] -= 1
            if j - i == 3:
                ans += 1
        return ans
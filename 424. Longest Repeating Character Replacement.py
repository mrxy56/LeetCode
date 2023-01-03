# 1. Sliding window, the key is maxfreq, which is greedy.
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        n = len(s)
        mp = defaultdict(int)
        j = 0
        ans = 0
        maxfreq = 0
        for i in range(n):
            mp[s[i]] += 1
            maxfreq = max(maxfreq, mp[s[i]])
            isvalid = (i + 1 - j - maxfreq <= k)
            if not isvalid:
                mp[s[j]] -= 1
                j += 1
            ans = max(ans, i - j + 1)
        return ans
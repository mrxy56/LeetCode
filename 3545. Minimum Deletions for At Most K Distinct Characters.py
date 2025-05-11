class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        mp = {}
        distinct = 0
        ans = 0
        for ch in s:
            if ch in mp:
                mp[ch] += 1
            else:
                mp[ch] = 1
                distinct += 1
        cnt = 1
        while distinct > k:
            for key, value in mp.items():
                if value == cnt:
                    mp[key] = -1
                    distinct -= 1
                    ans += value
                    if distinct == k:
                        break
            cnt += 1
        return ans
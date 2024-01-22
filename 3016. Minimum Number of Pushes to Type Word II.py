class Solution:
    def minimumPushes(self, word: str) -> int:
        cnt = [0 for i in range(26)]
        ans = 0
        for ch in word:
            cnt[ord(ch) - ord('a')] += 1
        ls = []
        for i in range(26):
            ls.append((i, cnt[i]))
        ls.sort(key = lambda x: -x[1])
        for i in range(26):
            x, num = ls[i]
            if i < 8:
                ans += num
            elif i >= 8 and i < 16:
                ans += num * 2
            elif i >= 16 and i < 24:
                ans += num * 3
            else:
                ans += num * 4
        return ans
class Solution:
    def numWays(self, s: str) -> int:
        pos = []
        for i, ch in enumerate(s):
            if ch == '1':
                pos.append(i)
        l = len(pos)
        n = len(s)
        if l == 0: # Combination
            tmp = (n - 1) * (n - 2) // 2
            return tmp % (10 ** 9 + 7) # parathesis
        if l % 3 != 0:
            return 0
        t = l // 3
        return (pos[t] - pos[t - 1]) * (pos[2 * t] - pos[2 * t - 1]) % (10 ** 9 + 7)
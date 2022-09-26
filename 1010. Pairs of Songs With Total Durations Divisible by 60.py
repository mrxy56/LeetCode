class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        d = {}
        ans = 0
        for t in time:
            t = t % 60
            if (60 - t) % 60 in d:
                ans += d[(60 - t) % 60]
            elif (120 - t) % 60 in d:
                ans += d[(120 - t) % 60] # (120 - t) % 60 should also be considered.
            if d.get(t):
                d[t] += 1
            else:
                d[t] = 1
        return ans
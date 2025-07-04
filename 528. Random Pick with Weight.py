# 1. Note that the randint should be [0, self.sum - 1], so that the probability can match.
class Solution:

    def __init__(self, w: List[int]):
        self.n = len(w)
        self.s = [0 for i in range(self.n)]
        self.sum = 0
        for i in range(self.n):
            if i == 0:
                self.s[i] = w[i]
            else:
                self.s[i] = self.s[i - 1] + w[i]
            self.sum += w[i]

    def pickIndex(self) -> int:
        r = random.randint(0, self.sum - 1)
        for i in range(self.n):
            if i == 0 and r >= 0 and r < self.s[0]:
                return 0
            if i > 0 and r >= self.s[i - 1] and r < self.s[i]:
                return i


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
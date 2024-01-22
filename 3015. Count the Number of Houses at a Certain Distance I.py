# 1. Do not use your brain to simulate it. For arbitrary two points, they either go from one to another directly, or through x, y, which ever is shorter.
# 2. x is not necessarily less than y, so make sure it in the beginning.
class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        ans = [0 for i in range(n)]
        if x > y:
            x, y = y, x
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                dis = min(j - i, abs(j - y) + abs(x - i) + 1)
                ans[dis - 1] += 2
        return ans
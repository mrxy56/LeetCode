# 1. Use nested defaultdict, payattention to the initialization which uses lambda.
# 2. Two cases, square can be above or below.
class DetectSquares:

    def __init__(self):
        from collections import defaultdict
        self.p = defaultdict(lambda: defaultdict(int))

    def add(self, point: List[int]) -> None:
        x, y = point
        self.p[x][y] += 1

    def count(self, point: List[int]) -> int:
        X, Y = point
        ans = 0
        for y in self.p[X]:
            if y == Y:
                continue
            else:
                d = abs(Y - y)
                ans += self.p[X][y] * self.p[X - d][Y] * self.p[X - d][y]
                ans += self.p[X][y] * self.p[X + d][Y] * self.p[X + d][y]
        return ans


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
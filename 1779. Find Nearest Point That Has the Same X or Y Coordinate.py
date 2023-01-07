class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        ind = -1
        dis = 2 << 31 - 1
        for i, point in enumerate(points):
            x0, y0 = point[0], point[1]
            if x0 == x or y0 == y:
                if abs(x - x0) + abs(y - y0) < dis:
                    dis = abs(x - x0) + abs(y - y0)
                    ind = i
        return ind
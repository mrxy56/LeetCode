# 1. Greedy, always select the interval with earlier end time.
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])
        ans = 1
        cur = points[0][1]
        for x, y in points:
            if cur < x:
                ans += 1
                cur = y
        return ans
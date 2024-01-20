# 1. Interval scheduling problem, notice x >= cur instead of x > cur.
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : x[1])
        cnt = 1
        cur = intervals[0][1]
        for x, y in intervals:
            if x >= cur:
                cnt += 1
                cur = y
        return len(intervals) - cnt
"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""
# 1. Sort and greedy. Gap can only exists in adjacant intervals.
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        ls = []
        for s in schedule:
            ls = ls + s
        ls = sorted(ls, key = lambda x: x.start)
        L, R, ans = 0, 0, []
        for i in range(1, len(ls)):
            L = max(L, ls[i - 1].end)
            R = ls[i].start
            if L < R:
                ans.append(Interval(L, R))
        return ans
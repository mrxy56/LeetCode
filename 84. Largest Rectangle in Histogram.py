# 1. This is a wise O(n) solution, needs to remember.
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s = [-1]
        max_area = 0
        n = len(heights)
        for i in range(n):
            while s[-1]!= -1 and heights[s[-1]] >= heights[i]:
                h = heights[s.pop()]
                w = i - s[-1] - 1
                print(h, w)
                max_area = max(max_area, h * w)
            s.append(i)
        while s[-1] != -1:
            h = heights[s.pop()]
            w = n - 1 - s[-1]
            max_area = max(max_area, h * w)
        return max_area
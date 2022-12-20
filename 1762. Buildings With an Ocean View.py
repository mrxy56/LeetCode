# 1. Ad hoc.
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        ans = []
        h = heights[-1]
        n = len(heights)
        ans.append(n - 1)
        for i in range(n - 2, -1, -1):
            if heights[i] > h:
                ans.append(i)
            h = max(h, heights[i])
        ans.sort()
        return ans
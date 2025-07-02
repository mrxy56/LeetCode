class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        ans = 0
        last = -1
        for t in timeSeries:
            if t <= last:
                ans += duration - (last - t + 1)
            else:
                ans += duration
            last = t + duration - 1
        return ans
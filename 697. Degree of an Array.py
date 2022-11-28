# 1. TLE in the beginning, try to record l, r in one setting.
# 2. We want the minimum length array, so try EVERY number that is eligible.
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        l = {}
        r = {}
        cnt = {}
        maxnum = 0
        for i, num in enumerate(nums):
            if not num in l:
                l[num] = i
            r[num] = i
            if not num in cnt:
                cnt[num] = 1
            else:
                cnt[num] += 1
            if cnt[num] > maxnum:
                maxnum = cnt[num]
        ans = 50000
        for k, v in cnt.items():
            if v == maxnum:
                ans = min(ans, r[k] - l[k] + 1)
        return ans
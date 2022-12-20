# 1. Prefix Sum + Two Sum.
# 2. Pay attention to the special case mp[0] = -1.
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        mp = {}
        mp[0] = -1
        ans = 0
        pre = 0
        for i, num in enumerate(nums):
            pre += num
            if pre - k in mp:
                ans = max(ans, i - mp[pre - k])
            if pre not in mp:
                mp[pre] = i
        return ans
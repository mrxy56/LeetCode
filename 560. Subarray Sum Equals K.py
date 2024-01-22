# 1. Using hash map and prefix sum.
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mp = {}
        ans = 0
        cur = 0
        for num in nums:
            cur += num
            if cur == k:
                ans += 1
            if cur - k in mp:
                ans += mp[cur - k]
            if cur in mp:
                mp[cur] += 1
            else:
                mp[cur] = 1
        return ans
            
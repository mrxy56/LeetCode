# Subarray is a hint to prefix sum, which is O(n) combined with dictionary.
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pre = [0 for i in range(n)]
        mp = Counter()
        ans = 0
        for i in range(n):
            if i > 0:
                pre[i] = (pre[i - 1] + nums[i]) % k
            else:
                pre[i] = nums[i] % k
            mp[pre[i]] += 1
        for k, v in mp.items():
            ans += (v * (v - 1)) // 2
            if k == 0:
                ans += v
        return ans
        
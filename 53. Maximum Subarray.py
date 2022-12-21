# 1. This makes me think about the gas station problem. For each start, the longer we go, the larger sum we can get. Unless adding this is worser than not adding it.
# 2. When that comes, simply use 0 to replace the negative value and start over again.
from collections import Counter
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [0 for i in range(n)]
        ans = dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(dp[i - 1], 0) + nums[i]
            ans = max(dp[i], ans)
        return ans
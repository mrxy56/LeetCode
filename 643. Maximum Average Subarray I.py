# 1. Sliding Window, would be hard if k is not fixed.
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans = - 10 ** 4
        tmp = 0
        n = len(nums)
        for i in range(k):
            tmp += nums[i]
        if tmp / k > ans:
            ans = tmp / k
        j = -1
        i = k - 1
        while i < n - 1:
            i += 1
            j += 1
            tmp += nums[i]
            tmp -= nums[j]
            if tmp / k > ans:
                ans = tmp / k
        return ans
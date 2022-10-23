class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans = nums[1] - nums[0] - 1
        n = len(nums)
        flag = 0
        for j in range(n):
            for i in range(j):
                if nums[j] - nums[i] > ans and nums[j] > nums[i]:
                    ans = nums[j] - nums[i]
                    flag = 1
        if flag:
            return ans
        else:
            return -1
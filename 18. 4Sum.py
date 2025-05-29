# 1. K sum turn to K - 1 sum.
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n):
            for j in range(i + 1, n):
                l = j + 1
                r = n - 1
                while l < r:
                    if target == nums[i] + nums[j] + nums[l] + nums[r]:
                        ans.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                    elif target > nums[i] + nums[j] + nums[l] + nums[r]:
                        l += 1
                    else:
                        r -= 1
        ans.sort()
        t = len(ans)
        ret = []
        for i in range(t):
            if i == 0:
                ret.append(ans[i])
            elif ans[i] != ans[i - 1]:
                ret.append(ans[i])
        return ret
                        
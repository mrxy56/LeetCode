# 1. Exactly greater or equal. Therefore, you need to check both sides.
# 2. N and n should be different, becasue we do not want the length to change.
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        N = n = len(nums)
        tmp = 0
        a = 0
        if n <= nums[0]:
            tmp = n
            a += 1
        n -= 1
        for i in range(1, N):
            if n <= nums[i] and n > nums[i - 1]:
                tmp = n
                a += 1
            n -= 1
        return tmp if a == 1 else -1
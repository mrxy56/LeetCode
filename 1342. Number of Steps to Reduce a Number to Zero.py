class Solution:
    def numberOfSteps(self, num: int) -> int:
        ans = 0
        while num:
            if num & 1:
                num = num - 1
            else:
                num = num >> 1
            ans += 1
        return ans
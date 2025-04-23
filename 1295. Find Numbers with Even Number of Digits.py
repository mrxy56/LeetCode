class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        def evenDigits(num):
            ans = 0
            while num:
                num = num // 10
                ans += 1
            if ans % 2 == 0:
                return True
            return False
        for num in nums:
            if evenDigits(num):
                ans += 1
        return ans
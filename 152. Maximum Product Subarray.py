# Each step, two options: start a subsequenc again, or add one sequence length.
# Record the historical maximum sequence.
# Recode min and max both since minus number exists.
# Not interval DP since it requires subsequences

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        cur_max = cur_min = 1
        if n == 1:
            return nums[0]
        ans = -100000000000
        for i in range(n):
            compares = [cur_max * nums[i], cur_min * nums[i], nums[i]]
            cur_max, cur_min = max(compares), min(compares)
            ans = max(ans, cur_max)
        return ans
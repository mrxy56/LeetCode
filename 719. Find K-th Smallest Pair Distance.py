class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def possible(guess):
            count = left = 0
            for right, x in enumerate(nums):
                while x - nums[left] > guess:
                    left += 1
                count += right - left # how many diffs?
            return count >= k
        nums.sort()
        lo = 0
        hi = nums[-1] - nums[0]
        while lo < hi:
            mi = (lo + hi) // 2 # wise, you binary search value
            if possible(mi):
                hi = mi
            else:
                lo = mi + 1
        return lo

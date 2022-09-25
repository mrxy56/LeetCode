class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        l = r = -1
        n = len(nums)
        if n == 0:
            return 0
        prev = nums[0] - 1
        ans = 0
        curlen = 0
        j = -1
        while j < n - 1:
            j += 1
            if nums[j] == prev + 1:
                curlen += 1
            elif nums[j] == prev: # longest sequence, not string, therefore, if same, continue
                continue
            else:
                curlen = 1
            ans = max(ans, curlen)
            prev = nums[j]
        return ans
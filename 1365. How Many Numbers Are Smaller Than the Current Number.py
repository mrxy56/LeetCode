class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        d = {}
        new_nums = sorted(nums)
        for i, num in enumerate(new_nums):
            if num not in d:
                d[num] = i # record first appearence
        ans = []
        for num in nums:
            ans.append(d[num])
        return ans
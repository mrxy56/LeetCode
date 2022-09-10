class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        ans = []
        for i, num in enumerate(nums):
            if target - num in d:
                ans.append(d[target - num])
                ans.append(i)
            d[num] = i
        return ans
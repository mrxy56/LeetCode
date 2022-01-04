# Just use list.count.
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        m = len(nums)/3
        ans = []
        s = set(nums)
        for num in s:
            if(nums.count(num) > m):
                ans.append(num)
        return ans
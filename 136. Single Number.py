class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}
        for num in nums:
            if not d.get(num):
                d[num] = 1
            else:
                d[num] += 1
        for k, v in d.items():
            if v % 2 == 1:
                return k
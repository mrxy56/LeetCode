class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        s = set()
        for num in nums:
            if num:
                s.add(num)
        return len(s)
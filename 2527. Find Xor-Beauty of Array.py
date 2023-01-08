# Symmetric, meaning changing two items, which will lead to same numbers with xor result to be 0.
class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        xor = 0
        for num in nums:
            xor = xor ^ num
        return xor

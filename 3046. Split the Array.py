class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        mp = {}
        for num in nums:
            if num in mp:
                mp[num] += 1
            else:
                mp[num] = 1
        for k, v in mp.items():
            if v > 2:
                return False
        return True
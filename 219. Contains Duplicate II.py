# I was thinking about priority queue, but set is easier. Remember the API set.remove().
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        s = set()
        for i in range(n):
            if nums[i] in s:
                return True
            s.add(nums[i])
            if len(s) > k:
                s.remove(nums[i - k])
        return False
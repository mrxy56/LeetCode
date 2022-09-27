class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        d = defaultdict(int)
        ans = 0
        for num in nums:
            d[num] += 1
        for i, value in d.items():
            if k > 0 and d[i] > 0 and d.get(i - k) and d[i - k] > 0: # since it is default dict, needs to get
                ans += 1
            if k == 0 and d[i] > 1: # k == 0 is special
                ans += 1
        return ans
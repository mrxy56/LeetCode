class Solution:

    def __init__(self, nums: List[int]):
        self.s = set(nums)
        self.original = nums
        self.n = len(nums)

    def reset(self) -> List[int]:
        return self.original

    def shuffle(self) -> List[int]:
        l = self.original
        ans = random.sample(l, self.n)
        return ans


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        for i in range(n):
            nums[i] = -nums[i]
        heapq.heapify(nums)
        for i in range(k):
            ans = heapq.heappop(nums)
        return -ans
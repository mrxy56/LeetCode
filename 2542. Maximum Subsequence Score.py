class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = [(a, b) for a, b in zip(nums1, nums2)]
        pairs.sort(key = lambda x: -x[1])
        ans = 0
        n = len(nums1)
        heap = [x[0] for x in pairs[:k]]
        tsum = sum(heap)
        heapq.heapify(heap)
        ans = tsum * pairs[k - 1][1]
        for i in range(k, n):
            tsum -= heapq.heappop(heap)
            tsum += pairs[i][0]
            heapq.heappush(heap, pairs[i][0])
            ans = max(ans, tsum * pairs[i][1])
        return ans
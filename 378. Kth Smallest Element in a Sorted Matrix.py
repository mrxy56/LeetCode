class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        ls = []
        for row in matrix:
            ls.extend(row)
        heapq.heapify(ls)
        for i in range(k):
            ans = heapq.heappop(ls)
        return ans
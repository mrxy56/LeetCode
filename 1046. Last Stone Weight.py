# 1. heapq APIs, heapq.heapify, heapq.heapop, heapq.heappush.
# 2. All the elements are negative, remember to recover them.
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n = len(stones)
        for i in range(n):
            stones[i] *= -1
        heapq.heapify(stones)
        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            if x != y:
                heapq.heappush(stones, x - y)
        return -stones[-1] if len(stones) else 0
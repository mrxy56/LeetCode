# 1. heapify is very important.
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        from collections import Counter
        from heapq import heapify, heappop

        words = Counter(words)
        heap = [(-freq, word) for word, freq in words.items()]
        heapify(heap)
        return [heappop(heap)[1] for i in range(k)]

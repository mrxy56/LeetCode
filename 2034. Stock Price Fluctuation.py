class StockPrice:
    def __init__(self):
        self.t = 0
        self.mp = {}
        self.min_heap = []
        self.max_heap = []

    def update(self, timestamp: int, price: int) -> None:
        import heapq
        self.mp[timestamp] = price
        self.t = max(self.t, timestamp)
        heapq.heappush(self.min_heap, (price, timestamp))
        heapq.heappush(self.max_heap, (-price, timestamp))

    def current(self) -> int:
        return self.mp[self.t]

    def maximum(self) -> int:
        price, t = self.max_heap[0]
        while -price != self.mp[t]:
            heapq.heappop(self.max_heap)
            price, t = self.max_heap[0]
        return -price

    def minimum(self) -> int:
        price, t = self.min_heap[0]
        while price != self.mp[t]:
            heapq.heappop(self.min_heap)
            price, t = self.min_heap[0]
        return price
        


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
class SmallestInfiniteSet:

    def __init__(self):
        self.heap = [i for i in range(1, 1001)]
        self.s = set(self.heap)

    def popSmallest(self) -> int:
        tmp = heapq.heappop(self.heap)
        self.s.remove(tmp)
        return tmp

    def addBack(self, num: int) -> None:
        if num not in self.s:
            heapq.heappush(self.heap, num)
            self.s.add(num)
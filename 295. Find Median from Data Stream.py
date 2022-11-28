# 1. O(n * log n) is not so slow since log n is actually nearly constant complexity.
class MedianFinder:

    def __init__(self):
        self.ls = []

    def addNum(self, num: int) -> None:
        self.ls.append(num)

    def findMedian(self) -> float:
        n = len(self.ls)
        self.ls.sort()
        if n % 2 == 1:
            return self.ls[n // 2]
        else:
            return (self.ls[n // 2] + self.ls[n // 2 - 1])/2
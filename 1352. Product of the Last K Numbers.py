class ProductOfNumbers:

    def __init__(self):
        self.l = [1] # The first one represents nothing or 0.

    def add(self, num: int) -> None:
        if num == 0:
            self.l = [1]
        else:
            self.l.append(self.l[-1] * num)


    def getProduct(self, k: int) -> int:
        n = len(self.l)
        if k < n: # only when k < n, we calculate, or else, it is 0.
            return self.l[n - 1] // self.l[n - k - 1]
        else:
            return 0
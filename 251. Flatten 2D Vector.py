class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.v = []
        for tv in vec:
            self.v += tv
        self.i = 0
        self.l = len(self.v)

    def next(self) -> int:
        if self.hasNext():
            ans = self.v[self.i] # index is tricky, be careful
            self.i += 1
            return ans

    def hasNext(self) -> bool:
        if self.i < self.l:
            return True
        return False
class MovingAverage:

    def __init__(self, size: int):
        self.sz = size
        self.q = []

    def next(self, val: int) -> float:
        self.q.append(val)
        tmp = 0
        qlen = len(self.q)
        cnt = 0
        for i in range(qlen - 1, -1, -1):
            if cnt == self.sz:
                break
            tmp += self.q[i]
            cnt += 1
        return tmp/cnt
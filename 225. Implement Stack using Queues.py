class MyStack:

    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        for i in range(len(self.q1) - 1):
            tmp = self.q1.pop(0)
            self.q2.append(tmp)
        ret = self.q1.pop(0)
        while len(self.q2) > 0:
            tmp = self.q2.pop(0)
            self.q1.append(tmp)
        return ret

    def top(self) -> int:
        for i in range(len(self.q1) - 1):
            tmp = self.q1.pop(0)
            self.q2.append(tmp)
        ret = self.q1.pop(0)
        self.q2.append(ret)
        while len(self.q2):
            tmp = self.q2.pop(0)
            self.q1.append(tmp)
        return ret

    def empty(self) -> bool:
        if len(self.q1) == 0:
            return True
        return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
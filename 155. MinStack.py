# 1. Pay attention to equal elements.
class MinStack:

    def __init__(self):
        self.s = []
        self.min_stack = []
        self.min_num = 2 ** 31 - 1
        self.len = 0

    def push(self, val: int) -> None:
        self.s.append(val)
        self.len += 1
        if val <= self.min_num:
            self.min_num = val
            self.min_stack.append(self.len - 1)

    def pop(self) -> None:
        if self.len - 1 == self.min_stack[-1]:
            self.min_stack.pop()
            if len(self.min_stack) > 0:
                self.min_num = self.s[self.min_stack[-1]]
            else:
                self.min_num = 2 ** 31 - 1
        self.s.pop()
        self.len -= 1

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.min_num


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
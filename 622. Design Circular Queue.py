# 1. Use a supertail. Don't forget mod.
class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [-1 for i in range(k)]
        self.head = 0
        self.tail = 0
        self.cnt = 0
        self.k = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.q[self.tail] = value
        self.tail = (self.tail + 1) % self.k
        self.cnt += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.q[self.head] = -1
        self.head = (self.head + 1) % self.k
        self.cnt -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[(self.tail - 1 + self.k) % self.k]
        
    def isEmpty(self) -> bool:
        if self.cnt == 0:
            return True
        return False

    def isFull(self) -> bool:
        if self.cnt == self.k:
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
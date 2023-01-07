# Maintain the number of consecutive values.
class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.last = 0
        self.tmp = 0
        self.ls = []

    def consec(self, num: int) -> bool:
        self.ls.append(num)
        if num == self.value:
            self.tmp += 1
        if len(self.ls) < self.k:
            return False
        if num == self.value:
            if self.tmp >= self.k:
                return True
        else:
            self.tmp = 0
            return False
            


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
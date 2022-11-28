# 1. Use queue and dictionary. System Design is just choosing the right Data Structure(s).
class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.maxNumbers = maxNumbers
        self.mp = {}
        self.q = []
        for i in range(maxNumbers):
            self.q.append(i)

    def get(self) -> int:
        if len(self.q) > 0:
            tmp = self.q.pop(0)
            self.mp[tmp] = 1
            return tmp
        else:
            return -1

    def check(self, number: int) -> bool:
        if number in self.mp:
            return False
        return True

    def release(self, number: int) -> None:
        if number in self.mp:
            del self.mp[number]
            self.q.append(number)


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
class TwoSum:

    def __init__(self):
        self.mp = {}
        self.sum_mp = {}

    def add(self, number: int) -> None:
        ls = []
        for k, v in self.mp.items():
            ls.append(k + number)
        for num in ls:
            self.sum_mp[num] = 1
        self.mp[number] = 1

    def find(self, value: int) -> bool:
        if value in self.sum_mp and self.sum_mp[value] == 1:
            return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
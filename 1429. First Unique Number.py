class FirstUnique:

    def __init__(self, nums: List[int]):
        self.n = nums
        self.mp = {}
        self.ind = -1
        self.cnt = len(nums)
        for num in self.n:
            if num in self.mp:
                self.mp[num] += 1
            else:
                self.mp[num] = 1
        for i, num in enumerate(self.n):
            if self.mp[num] == 1:
                self.ind = i
                break
        return

    def showFirstUnique(self) -> int:
        if self.ind != -1 and self.ind < self.cnt:
            return self.n[self.ind]
        else:
            return -1

    def add(self, value: int) -> None:
        self.n.append(value)
        self.cnt += 1
        if value in self.mp:
            self.mp[value] += 1
        else:
            self.mp[value] = 1
        if value == self.n[self.ind]:
            while self.ind < self.cnt and self.mp[self.n[self.ind]] > 1:
                self.ind += 1
        return


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
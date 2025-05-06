class MyHashSet:

    def __init__(self):
        self.s = [0 for i in range(10 ** 6 + 1)]
        

    def add(self, key: int) -> None:
        self.s[key] = 1

    def remove(self, key: int) -> None:
        self.s[key] = 0

    def contains(self, key: int) -> bool:
        if self.s[key] == 1:
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
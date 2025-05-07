class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.mp = {}
        for word in dictionary:
            n = len(word)
            if n <= 2:
                if word not in self.mp:
                    self.mp[word] = set(word)
            else:
                abbr = word[0] + str(n - 2) + word[-1]
                if abbr not in self.mp:
                    self.mp[abbr] = set()
                    self.mp[abbr].add(word)
                else:
                    self.mp[abbr].add(word)
                

    def isUnique(self, word: str) -> bool:
        n = len(word)
        abbr = word[0] + str(n - 2) + word[-1]
        if abbr not in self.mp or word in self.mp[abbr] and len(self.mp[abbr]) == 1:
            return True
        return False


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
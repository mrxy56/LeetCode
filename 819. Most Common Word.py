class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        pattern = '\w+' #regular expression
        words = re.findall(pattern, paragraph)
        self.d = {}
        for word in words:
            if self.d.get(word):
                self.d[word] += 1
            else:
                self.d[word] = 1
        def myFunc(w):
            return self.d[w]
        words.sort(key = myFunc, reverse = True) # sort according to index
        banned = set(banned)
        for word in words:
            if word not in banned:
                return word
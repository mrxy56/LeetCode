class Solution:
    def longestWord(self, words: List[str]) -> str:
        d = defaultdict(int)
        for word in words:
            d[word] += 1
        ans = ""
        words.sort()
        n = len(words)
        for i in range(n - 1, -1, -1):
            word = words[i]
            l = len(word)
            if len(word) > len(ans) or len(word) == len(ans) and word < ans: # This is wise, like calculating minimum.
                flag = True
                for k in range(1, l):
                    if word[:k] not in d:
                        flag = False
                if flag:
                    ans = word
        return ans
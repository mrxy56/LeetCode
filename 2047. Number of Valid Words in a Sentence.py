class Solution:
    def countValidWords(self, sentence: str) -> int:
        words = sentence.split(' ')
        words = list(filter(None, words)) # Filter should be wrapped up by list.
        ans = 0
        for word in words:
            flag = True
            punc = 0
            hyphen = 0
            for i, ch in enumerate(word):
                if ch.isdigit():
                    flag = False
                    break
                if ch == '-':
                    hyphen += 1
                    if i == 0 or i == len(word) - 1 or hyphen >= 2:
                        flag = False
                        break
                    if not (word[i - 1].isalpha() and word[i + 1].isalpha()): # must notice that '-' must be surrounded by alphabets.
                        flag = False
                        break
                if ch == '!' or ch == '.' or ch == ',':
                    punc += 1
                    if i != len(word) - 1 or punc >= 2:
                        flag = False
                        break
            if flag:
                ans += 1
        return ans
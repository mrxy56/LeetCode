# 1. Logic must be clear.
class Solution:
    def isValid(self, word: str) -> bool:
        flag1 = 0
        flag2 = 0
        vowel = set(['a', 'e', 'i', 'o', 'u'])
        if len(word) < 3:
            return False
        for ch in word:
            if not (ch.isalpha() or ch.isdigit()):
                return False
            if ch.lower() in vowel:
                flag1 = 1
            elif ch.isalpha() and ch.lower() not in vowel:
                flag2 = 1
        if flag1 == 0 or flag2 == 0:
            return False
        return True
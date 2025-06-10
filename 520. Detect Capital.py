class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        n = len(word)
        s = 0
        l = 0
        for i in range(n):
            if word[i] >= 'a' and word[i] <= 'z':
                s += 1
            elif word[i] >= 'A' and word[i] <= 'Z':
                l += 1
        if s == n or l == n:
            return True
        if s == n - 1 and word[0] >= 'A' and word[0] <= 'Z':
            return True
        return False
            
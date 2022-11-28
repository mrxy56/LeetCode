# 1. Simplified text justification, pay attention to the edge cases.
class Solution:
    def reorderSpaces(self, text: str) -> str:
        spaces = 0
        for ch in text:
            if ch == ' ':
                spaces += 1
        words = text.split()
        n = len(words)
        if n == 1:
            return text.strip() + ' ' * spaces
        tmp = ""
        end = ""
        for i in range(spaces // (n - 1)):
            tmp += ' '
        for i in range(spaces % (n - 1)):
            end += ' '
        ans = ""
        for i in range(n - 1):
            ans += words[i]
            ans += tmp
        ans += words[n - 1] + end
        return ans
        
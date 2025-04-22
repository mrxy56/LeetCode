# 1. Instead of passing the part of string/list itself (will create a new string and won't change the original one) to the function, 
# pass the whole string's reference and index. If you want to use function.
class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def swapStr(s):
            n = len(s)
            for i in range(n // 2):
                s[i], s[n - 1 - i] = s[n - 1 - i], s[i]
        i = j = 0
        n = len(s)
        for k in range(n // 2):
                s[k], s[n - 1 - k] = s[n - 1 - k], s[k]
        i = 0
        for j in range(n + 1):
            if j == n or s[j] == ' ':
                for k in range((j - i)//2):
                    s[i + k], s[j - 1 - k] = s[j - 1 - k], s[i + k]
                i = j + 1
        return s
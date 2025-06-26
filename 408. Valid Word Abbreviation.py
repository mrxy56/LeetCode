# 1. Too many edge cases.
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0
        j = 0
        n = len(word)
        m = len(abbr)
        while i < n and j < m:
            if abbr[j].isdigit():
                cnt = 0
                if j + 1 < m and abbr[j] == '0' and abbr[j + 1] != '0':
                    return False
                while j < m and abbr[j].isdigit():
                    cnt = cnt * 10 + ord(abbr[j]) - ord('0')
                    j += 1
                for k in range(cnt):
                    i += 1
                    if k < cnt - 1 and i == n:
                        return False
                if i >= n and j < m or j >= m and i < n:
                    return False
            elif word[i] != abbr[j]:
                return False
            elif word[i] == abbr[j]:
                i += 1
                j += 1
        if i == n and j < m or i < n and j == m:
            return False
        return True
            
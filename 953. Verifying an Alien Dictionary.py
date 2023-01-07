# 1. Clever way to use loop. app < apple.
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mp = {}
        for i, val in enumerate(order):
            mp[val] = i
        for i in range(len(words) - 1):
            for j in range(len(words[i])):
                if j >= len(words[i + 1]):
                    return False
                if mp[words[i][j]] != mp[words[i + 1][j]]:
                    if mp[words[i][j]] > mp[words[i + 1][j]]:
                        return False
                    break
        return True
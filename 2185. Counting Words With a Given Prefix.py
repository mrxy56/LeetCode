class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        ans = 0
        n = len(pref)
        for word in words:
            if word[:n] == pref:
                ans += 1
        return ans
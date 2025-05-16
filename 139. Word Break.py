class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        m = len(wordDict)
        @lru_cache()
        def dp(num):
            if num == n:
                return True
            for i in range(m):
                l = len(wordDict[i])
                if wordDict[i] == s[num: num + l]:
                    if dp(num + l):
                        return True
            return False
        return dp(0)
            
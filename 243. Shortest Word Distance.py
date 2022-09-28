class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        ans = len(wordsDict)
        l = r = -1
        for i, w in enumerate(wordsDict):
            if w == word1:
                l = i
            if w == word2:
                r = i
            if l >= 0 and r >= 0:
                ans = min(ans, abs(l - r)) # greedy, maintain the current place, every crucial point, update
        return ans
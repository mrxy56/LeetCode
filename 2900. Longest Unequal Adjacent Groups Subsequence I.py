class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        ans = []
        for i in range(n):
            if i == 0 or groups[i] != groups[i - 1]:
                ans.append(words[i])
        return ans
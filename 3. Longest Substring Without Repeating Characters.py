class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = Counter()
        i = j = ans = 0
        while j < len(s): # sliding window
            d[s[j]] += 1
            while d[s[j]] > 1: # find repeat in the previous inteval
                d[s[i]] -= 1 # locate the repeat
                i += 1
            ans = max(ans, j - i + 1)
            j += 1
        return ans
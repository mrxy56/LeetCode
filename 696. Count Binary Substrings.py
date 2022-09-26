class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        groups = [1]
        for i in range(1, len(s)):
            if s[i - 1] != s[i]: # a wise way to calculate groups
                groups.append(1)
            else:
                groups[-1] += 1
        ans = 0
        for i in range(1, len(groups)): # operate through groups to avoid TLE.
            ans += min(groups[i - 1], groups[i])
        return ans
# 1. Ordinary Sliding Window problem. 
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = set(['a','e','i','o','u'])
        j = -1
        n = len(s)
        ans = tmp = 0
        for i in range(k):
            if s[i] in vowel:
                tmp += 1
        if tmp > ans:
            ans = tmp
        i = k - 1
        while i < n - 1:
            i += 1
            if s[i] in vowel:
                tmp += 1
            j += 1
            if s[j] in vowel:
                tmp -= 1
            if tmp > ans:
                ans = tmp
        return ans
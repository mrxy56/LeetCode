# 1. I was almost correct except that repeating caused TLE. We do not need to reconstruct the string again and do the verification from the scratch.
# 2. Adding indexes, so that we only need to focus on the rest part.
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def ispalindrome(s, i, j):
            while i < j:
                if s[i]!=s[j]:
                    return False
                i += 1
                j -= 1
            return True

        i = 0
        j = len(s) - 1
        if ispalindrome(s, i, j):
            return True

        while i < j:
            if s[i]!= s[j]:
                if ispalindrome(s, i, j - 1) or ispalindrome(s, i + 1, j):
                    return True
                return False
            i += 1
            j -= 1
        return False
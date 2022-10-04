class Solution:
    def canPermutePalindrome(self, s: str) -> bool: # The definition of permutation is any combinations of the letters.
        return sum(v % 2 for v in Counter(s).values()) < 2
# 1. Just to compare if the number of characters are equal accoudingly.
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        s1 = set(word1)
        s2 = set(word2)
        from collections import Counter
        mp1 = Counter()
        mp2 = Counter()
        l1 = []
        l2 = []
        if len(word1) != len(word2) or s1 != s2:
            return False
        n = len(word1)
        for i in range(n):
            mp1[word1[i]] += 1
            mp2[word2[i]] += 1
        for k, v in mp1.items():
            l1.append(v)
        for k, v in mp2.items():
            l2.append(v)
        m = len(l1)
        l1.sort()
        l2.sort()
        for i in range(m):
            if l1[i] != l2[i]:
                return False
        return True
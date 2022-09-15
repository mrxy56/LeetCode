class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        ans = []
        from collections import defaultdict
        d2 = defaultdict(int)
        for word2 in words2:
            t2 = defaultdict(int)
            for c in word2:
                t2[c] += 1
                d2[c] = max(d2[c], t2[c]) # Do not use O(n^2), unite all the words in list2 first
        for word1 in words1:
            flag = 1
            d1 = defaultdict(int)
            for c in word1:
                d1[c] += 1
            for k, v in d2.items():
                if d1[k] < d2[k]:
                    flag = 0
                    break
            if flag:
                ans.append(word1)
        return ans
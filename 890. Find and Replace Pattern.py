# 1. Mapping is a two-way mapping. So check in two ways.
# 2. Cannot use offset in this problem.
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans = []
        for word in words:
            if len(word) != len(pattern):
                continue
            flag = True
            mp = {}
            s = set()
            for i, ch in enumerate(word):
                if pattern[i] not in mp:
                    mp[pattern[i]] = ch
                    if ch in s:
                        flag = False
                        break
                    s.add(ch)
                elif mp[pattern[i]] != ch:
                    flag = False
                    break
            if flag:
                ans.append(word)
        return ans
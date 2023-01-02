# 1. Many edge cases.
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1 = []
        s2 = []
        for ch in s:
            if ch == '#' and len(s1):
                s1.pop()
            elif ch == '#' and len(s1) == 0:
                continue
            else:
                s1.append(ch)
        for ch in t:
            if ch == '#' and len(s2):
                s2.pop()
            elif ch == '#' and len(s2) == 0:
                continue
            else:
                s2.append(ch)
        str1 = "".join(s1)
        str2 = "".join(s2)
        return True if str1 == str2 else False
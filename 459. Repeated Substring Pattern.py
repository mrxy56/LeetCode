# 1. There is also an O(n) solution.
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for k in range(1, n + 1):
            last = ""
            flag = True
            cnt = 0
            for i in range(0, n, k):
                if i + k > n:
                    flag = False
                    break
                tmp = s[i:i + k]
                cnt += 1
                if last and tmp != last:
                    flag = False
                    break
                last = tmp
            if flag and cnt >= 2:
                return True
        return False
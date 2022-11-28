# 1. Ad hoc.
class Solution:
    def checkRecord(self, s: str) -> bool:
        n = len(s)
        absent = 0
        for i in range(n):
            if s[i] == 'A':
                absent += 1
            if s[i] == 'L' and i <= n - 3:
                if s[i + 1] == 'L' and s[i + 2] == 'L':
                    return False
        if absent >= 2:
            return False
        return True
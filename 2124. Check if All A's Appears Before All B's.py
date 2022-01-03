class Solution:
    def checkString(self, s: str) -> bool:
        flag = False
        for ch in s[::-1]:
            if ch == 'a':
                flag = True
            if ch == 'b' and flag:
                return False
        return True
        
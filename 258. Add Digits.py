class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num)) > 1:
            tmp = 0
            for ch in str(num):
                tmp += int(ch)
            num = tmp
        return num  
class Solution:
    def convertToBase7(self, num: int) -> str:
        s = ""
        if num == 0:
            return "0"
        flag = 0
        if num < 0:
            num *= -1
            flag = 1
        while num:
            s += str(num % 7)
            num = num // 7
        if flag:
            return "-" + s[::-1]
        else:
            return s[::-1]
        
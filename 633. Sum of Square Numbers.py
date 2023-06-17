class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        b = int(sqrt(c))
        a = 0
        while a <= b:
            if a * a + b * b == c:
                return True
            elif a * a + b * b < c:
                a += 1
            else:
                b -= 1
        return False
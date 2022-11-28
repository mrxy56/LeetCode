# 1. Cannot iterate one by one, will cause TLE.
# 2. Only consider i * i <= num and num // i.
# 3. Subtract num itself finally.
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        ls = []
        i = 1
        ans = 0
        while i * i <= num:
            if num % i == 0:
                ans += i
                if i * i != num:
                    ans += num // i
            i += 1
        return num == (ans - num)
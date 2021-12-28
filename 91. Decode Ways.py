# State i can came from i - 1 and i - 2, pay attention to those numbers that start with 0, which is not valid.
class Solution:
    def numDecodings(self, s: str) -> int:
        def decode(code):
            if code[0] == '0':
                return 0
            return int(code)
        def is_valid(num):
            if num >= 1 and num <= 26:
                return True
            return False
            
        n = len(s)
        dp = [0 for i in range(n)]
        if is_valid(decode(s[0])):
            dp[0] = 1
        else:
            return 0
        if n >= 2:
            if is_valid(decode(s[0:2])):
                dp[1] += 1
            if is_valid(decode(s[1:2])):
                dp[1] += dp[0]
        for i in range(2, n):
            for step in range(2):
                tmp = decode(s[i - step: i + 1])
                if is_valid(tmp):
                    dp[i] += dp[i - step - 1]
        return dp[n - 1]
        
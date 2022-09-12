class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        longest = 0
        ss = 0
        ts = 0
        dp = [[0 for j in range(l)] for i in range(l)]
        for i in range(l):
            dp[i][i] = 1
            if dp[i][i] > longest:
                ss = i
                tt = i
        for i in range(l - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = 2
                if dp[i][i + 1] > longest:
                    ss = i
                    tt = i + 1
        for i in range(1, l - 1):
            for j in range(1, i + 1):
                if i - j >= 0 and i + j < l:
                    if s[i - j] == s[i + j] and dp[i - j + 1][i + j - 1]:
                        dp[i - j][i + j] = dp[i - j + 1][i + j - 1] + 2
                        if dp[i - j][i + j] > longest:
                            longest = dp[i - j][i + j]
                            ss = i - j 
                            tt = i + j
                else:
                    break
        for i in range(1, l - 1):
            for j in range(1, i + 1): # Pay attention of the choosing of j
                if i - j >= 0 and i + j + 1 < l:
                    if s[i - j] == s[i + j + 1] and dp[i - j + 1][i + j]:
                        dp[i - j][i + j + 1] = dp[i - j + 1][i + j] + 2
                        if dp[i - j][i + j + 1] > longest:
                            longest = dp[i - j][i + j + 1]
                            ss = i - j
                            tt = i + j + 1
                else:
                    break
        return s[ss: tt + 1]
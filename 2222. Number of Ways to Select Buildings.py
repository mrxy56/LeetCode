class Solution:
    def numberOfWays(self, s: str) -> int:
        l = len(s)
        dp0 = [0 for i in range(l)] # Two DP arrays
        dp1 = [0 for i in range(l)]
        for i in range(l):
            if s[i] == '0':
                dp0[i] += 1
            else:
                dp1[i] += 1
        cnt0 = 0
        cnt1 = 0
        for i in range(l):
            if s[i] == '0':
                cnt0 += dp0[i] # update cnt0
                dp0[i] = cnt1  # assign dp0
            else:
                cnt1 += dp1[i] # update cnt1
                dp1[i] = cnt0 # assign dp1
        cnt0 = 0
        cnt1 = 0
        for i in range(l):
            if s[i] == '0':
                cnt0 += dp0[i] 
                dp0[i] = cnt1
            else:
                cnt1 += dp1[i]
                dp1[i] = cnt0
        ans = 0
        for i in range(l):
            ans += dp0[i] + dp1[i]
        return ans
                
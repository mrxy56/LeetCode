class Solution:
    def confusingNumber(self, n: int) -> bool:
        mp = {0:0, 1:1, 6:9, 8:8, 9:6}
        s = str(n)
        ans = 0
        while n:
            if n % 10 not in mp:
                return False
            else:
                ans = ans * 10 + mp[n % 10]
                n = n // 10
        if str(ans) == s:
            return False
        return True 
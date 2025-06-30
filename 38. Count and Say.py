class Solution:
    def countAndSay(self, n: int) -> str:
        def dfs(n):
            if n == 1:
                return "1"
            s = dfs(n - 1)
            l = len(s)
            cnt = 0
            ans = []
            for i in range(l + 1):
                if i == l or i > 0 and s[i] != s[i - 1]:
                    ans.append(str(cnt))
                    ans.append(s[i - 1])
                    cnt = 1
                else:
                    cnt += 1
            return "".join(ans)
        return dfs(n)
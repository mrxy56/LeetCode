class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(p)
        tmp = []
        for i in range(m):
            if i == 0:
                tmp.append(p[i])
            elif p[i] == '*':
                if p[i] != tmp[-1]:
                    tmp.append(p[i])
            else:
                tmp.append(p[i])
        p = "".join(tmp)
        @lru_cache(None)
        def dfs(s, p):
            i = 0
            j = 0
            n = len(s)
            m = len(p)
            if n == 0 and len(p) == 1 and p[0] == '*':
                return True
            while i < n and j < m:
                if s[i] == p[j] or p[j] == '?':
                    i += 1
                    j += 1
                elif p[j] == '*':
                    while i < n:
                        if j == m - 1:
                            return True
                        elif s[i] == p[j + 1] or p[j + 1] == '?':
                            flag = dfs(s[i:], p[j + 1:])
                            if flag:
                                return True
                        i += 1
                elif s[i] != p[j]:
                    return False
            if i == n and j == m:
                return True
            if i == n and j == m - 1 and p[-1] == '*':
                return True
            return False
        return dfs(s, p)
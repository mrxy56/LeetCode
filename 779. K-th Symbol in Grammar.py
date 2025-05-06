class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def dfs(n, k):
            if n == 1 and k == 0:
                return 0
            ret = dfs(n - 1, k // 2)
            if ret == 0:
                if k % 2 == 0:
                    return 0
                else:
                    return 1
            elif ret == 1:
                if k % 2 == 0:
                    return 1
                else:
                    return 0
              
        return dfs(n, k - 1)
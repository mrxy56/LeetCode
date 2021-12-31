# Do not use interval DP because the state means how many palindrome cuts we have, but very hard to backtrack.
# Simply use DFS to cut.
# s[::-1] means reversed string.
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        ans = []
        def dfs(ls, start):
            if start == n:
                ans.append(ls)
                return
            for i in range(start + 1, n + 1):
                tmp = s[start:i]
                if tmp == tmp[::-1]:
                    dfs(ls + [tmp], i)
        dfs([], 0)
        return ans
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        vis = [0 for i in range(10)]
        ans = []
        def dfs(s, num, last, ls):
            if s > n or num > k:
                return
            if s == n and num == k:
                ans.append(list(ls))
            for i in range(1, 10):
                if i > last and not vis[i]:
                    vis[i] = 1
                    dfs(s + i, num + 1, i, ls + [i])
                    vis[i] = 0
            return 
        dfs(0, 0, 0, [])
        return ans